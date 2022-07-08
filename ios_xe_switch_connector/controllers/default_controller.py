from asyncio.log import logger
import json
import re
import connexion
import six
import requests
from ios_xe_switch_connector import util
import os
from dotenv import load_dotenv
from ios_xe_switch_connector.models.vlan_info import VlanInfo  # noqa: E501

load_dotenv()


def create_vlan(body):  # noqa: E501
    """create vlan

    Create a vlan for a device interface  # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: str
    """

    hst = os.getenv('HOST')
    if connexion.request.is_json:
        body = VlanInfo.from_dict(connexion.request.get_json())  # noqa: E501
        name = body.interface_name
        vlan = body.vlan_number
        
        regex = r'^([^\d]+)(\d+.*)$'
        splitted_iface = re.search(regex, name)

        body_a = {
            f"Cisco-IOS-XE-native:{splitted_iface[1]}": [
                {
                    "name": splitted_iface[2],
                    "switchport": {
                        "Cisco-IOS-XE-switch:access": {
                            "vlan": {
                                "vlan": vlan
                            }
                        }
                    }}]}
        api_url = f'https://{hst}:443/restconf/data/Cisco-IOS-XE-native:native/interface/{splitted_iface[1]}'
        headers = {'Accept': 'application/yang-data+json', 'Content-Type': 'application/yang-data+json'}
        response = requests.patch(api_url, verify=False, headers=headers,
                                  auth=(os.getenv('USRNAME'), os.getenv('PASSWORD')), data=json.dumps(body_a))
        return f"patch completed vlan {vlan} created on the interface {name}"


def get_vlan():  # noqa: E501
    """get vlans

    Get all vlans on a switch.  # noqa: E501


    :rtype: str
    """
    hst = os.getenv('HOST')
    headers = {'Accept': 'application/yang-data+json'}
    api_url = f'https://{hst}:443/restconf/data/Cisco-IOS-XE-vlan-oper:vlans/vlan'
    response = requests.get(api_url, verify=False, headers=headers, auth=(
        os.getenv('USRNAME'), os.getenv('PASSWORD')))
    return response.json()

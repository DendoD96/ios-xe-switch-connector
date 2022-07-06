from asyncio.log import logger
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
    if connexion.request.is_json:
        body = VlanInfo.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_vlan():  # noqa: E501
    """get vlans

    Get all vlans on a switch.  # noqa: E501


    :rtype: str
    """
    hst = os.getenv('HOST')
    headers = {'Accept':'application/yang-data+json'}
    api_url = f'https://{hst}:443/restconf/data/Cisco-IOS-XE-vlan-oper:vlans/vlan'
    response = requests.get(api_url, verify = False, headers = headers, auth = (os.getenv('USRNAME'), os.getenv('PASSWORD')))
    return response.json()
from asyncio.log import logger
import connexion
import six
import requests
from ios_xe_switch_connector import util
import os
from dotenv import load_dotenv

load_dotenv()

def say_hello():
    """say hello

    Simple API that hails.


    :rtype: str
    """
    hst = os.getenv('HOST')
    headers = {'Accept':'application/yang-data+json'}
    api_url = f'https://{hst}:443/restconf/data/Cisco-IOS-XE-vlan-oper:vlans/vlan'
    response = requests.get(api_url, verify = False, headers = headers, auth = (os.getenv('USRNAME'), os.getenv('PASSWORD')))
    return response.json()
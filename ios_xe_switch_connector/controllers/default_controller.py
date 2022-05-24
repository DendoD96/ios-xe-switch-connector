from asyncio.log import logger
import connexion
import six

from ios_xe_switch_connector import util


def say_hello():
    """say hello

    Simple API that hails.


    :rtype: str
    """
    return 'Hello World!'

# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "ios_xe_switch_connector"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion",
    "swagger-ui-bundle>=0.0.2"
]

setup(
    name=NAME,
    version=VERSION,
    description="IOS-XE switches connector",
    author_email="daniele.rossi@vem.com",
    url="",
    keywords=["Swagger", "IOS-XE switches connector"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['ios_xe_switch_connector=ios_xe_switch_connector.__main__:main']},
    long_description="""\
    Connector API to Cisco IOS-XE switches
    """
)

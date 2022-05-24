# coding: utf-8

from __future__ import absolute_import

from ios_xe_switch_connector.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_say_hello(self):
        """Test case for say_hello

        say hello
        """
        response = self.client.open(
            '/hello',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

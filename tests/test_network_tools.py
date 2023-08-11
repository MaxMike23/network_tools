import unittest
import subprocess
from NetworkTools.network_tools import *

class TestNetworkTools(unittest.TestCase):
    """ Test NetworkTools """

    def test_interface_is_connected(self):
        """ Tests for active interfaces """
        self.assertEqual(interface_is_connected(), True)




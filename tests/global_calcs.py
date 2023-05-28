"""
This is the tests of global/general calculations module of pyclc

Author: Leo Araya

Type: Unittests
"""

import unittest

from pyclc import General

class TestGeneral(unittest.TestCase):
    """Test the general calculations module of pyclc"""
    def setUp(self):
        """Set up the test"""
        self.general = General()
    
    def test_get_average(self):
        """> Should return the average of a list of numbers"""
        self.assertEqual(self.general.get_average([1, 2, 3, 4, 5]))

    def test_get_imc(self):
        """> Should return the imc of a person"""
        self.assertEqual(self.general.imc(1.80, 80))    

if __name__ == '__main__':
    unittest.main()
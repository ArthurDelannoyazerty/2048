import unittest
import constants

class TestConstants(unittest.TestCase):

    def test_BackGroundColorDict(self): 
        """Test that a number absent in the dict return the #ffffff color"""
        self.assertEqual(constants.BACKGROUND_COLOR_DICT[0], "#ffffff")
    
    def test_ForeGroundColorDict(self): 
        """Test that a number absent in the dict return the #000000 color"""
        self.assertEqual(constants.FOREGROUND_COLOR_DICT[0], "#000000")



if __name__ == '__main__':
    unittest.main()
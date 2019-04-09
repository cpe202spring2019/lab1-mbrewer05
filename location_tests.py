import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc1 = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc1),"Location('SLO', 35.3, -120.7)")
    
    # Add more tests!
    def test_eq(self):
        loc1 = Location("SLO", 35.3, -120.7)
        #test correct
        loc2 = Location("SLO", 35.3, -120.7)
        self.assertTrue(loc1 == loc2)
        #one variable wrong
        loc2 = Location("SLO", 35.3, 56.2)
        self.assertFalse(loc1 == loc2)
        loc2 = Location("SLO", 17.43, -120.7)
        self.assertFalse(loc1 == loc2)
        loc2 = Location("BAY", 35.3, -120.7)
        self.assertFalse(loc1 == loc2)
        #two variables wrong
        loc2 = Location("SLO", 90.0, 532.7)
        self.assertFalse(loc1 == loc2)
        loc2 = Location("KARS", 35.3, 7.65)
        self.assertFalse(loc1 == loc2)
        loc2 = Location("WHAM", 35.93, -120.7)
        self.assertFalse(loc1 == loc2)
        #all variable wrong
        loc2 = Location("WHAM", 35.93, 90.87)
        self.assertFalse(loc1 == loc2)
        #not a Location
        self.assertFalse(loc1 == '4')
        

if __name__ == "__main__":
        unittest.main()

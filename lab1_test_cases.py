import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        #check ValueError case
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        #check when list is empty
        lst = []
        self.assertIsNone(max_list_iter(lst))

        #check when there is one max value
        lst = [5,2,3,4]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [1,5,3,4]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [1,2,5,4]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [1,2,3,5]
        self.assertEqual(max_list_iter(lst), 5)

        #check when there are two max values
        lst = [5,5,3,4]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [5,2,5,4]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [5,2,3,5]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [1,5,5,4]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [1,5,3,5]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [1,2,5,5]
        self.assertEqual(max_list_iter(lst), 5)

        #check when there are three max values
        lst = [5,5,5,4]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [5,5,3,5]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [5,2,5,5]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [1,5,5,5]
        self.assertEqual(max_list_iter(lst), 5)

        #check when there are all max values
        lst = [5,5,5,5]
        self.assertEqual(max_list_iter(lst), 5)

        #list of various lengths
        lst = [1,5,3]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [5,3]
        self.assertEqual(max_list_iter(lst), 5)
        lst = [5]
        self.assertEqual(max_list_iter(lst), 5)
        

    def test_reverse_rec(self):
        #check value error case
        with self.assertRaises(ValueError):
            reverse_rec(None)

        #ordered list
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

        #duplicate numbers
        self.assertEqual(reverse_rec([1,3,3]),[3,3,1])
        self.assertEqual(reverse_rec([3,3,1]),[1,3,3])

        #all the same number
        self.assertEqual(reverse_rec([3,3,3]),[3,3,3])

        #random list
        self.assertEqual(reverse_rec([8,-56,86]),[86,-56,8])

        #list of different lengths
        self.assertEqual(reverse_rec([8, 86]),[86, 8])
        self.assertEqual(reverse_rec([8]),[8])

        #check an empty list
        self.assertEqual(reverse_rec([]), [])


    def test_bin_search(self):
        #test value error case
        with self.assertRaises(ValueError):
            lst = None
            bin_search(4, 0, 5, lst)

        #test value is in different places
        list_val = [0,1,2,3,4,7,8,9,10]
        self.assertEqual(bin_search(0, 0, len(list_val)-1, list_val), 0)
        self.assertEqual(bin_search(1, 0, len(list_val)-1, list_val), 1)
        self.assertEqual(bin_search(2, 0, len(list_val)-1, list_val), 2)
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 3)
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4)
        self.assertEqual(bin_search(7, 0, len(list_val)-1, list_val), 5)
        self.assertEqual(bin_search(8, 0, len(list_val)-1, list_val), 6)
        self.assertEqual(bin_search(9, 0, len(list_val)-1, list_val), 7)
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 8)

        #test value missing in different places
        list_val = [-1,1,2,3,4,7,8,9,10]
        self.assertIsNone(bin_search(-2, 0, len(list_val)-1, list_val))
        list_val = [-1,1,2,3,4,7,8,9,10]
        self.assertIsNone(bin_search(0, 0, len(list_val)-1, list_val))
        list_val = [-1,0,2,3,4,7,8,9,10]
        self.assertIsNone(bin_search(1, 0, len(list_val)-1, list_val))
        list_val = [-1,0,1,3,4,7,8,9,10]
        self.assertIsNone(bin_search(2, 0, len(list_val)-1, list_val))
        list_val = [-1,0,2,3,5,7,8,9,10]
        self.assertIsNone(bin_search(4, 0, len(list_val)-1, list_val))
        list_val = [-1,0,2,3,4,7,8,9,10]
        self.assertIsNone(bin_search(5, 0, len(list_val)-1, list_val))
        list_val = [-1,0,2,3,5,6,8,9,10]
        self.assertIsNone(bin_search(7, 0, len(list_val)-1, list_val))
        list_val = [-1,0,2,3,5,6,7,9,10]
        self.assertIsNone(bin_search(8, 0, len(list_val)-1, list_val))
        list_val = [-1,0,2,3,5,6,7,8,10]
        self.assertIsNone(bin_search(9, 0, len(list_val)-1, list_val))
        list_val = [-1,0,2,3,5,6,7,8,9]
        self.assertIsNone(bin_search(10, 0, len(list_val)-1 , list_val))
        

        #test when point is out of range
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertIsNone(bin_search(0, 3, len(list_val)-1, list_val))
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertIsNone(bin_search(10, 0, len(list_val)-4, list_val))
        list_val =[0,1,2,3,4,7,8,9,10]
        self.assertIsNone(bin_search(10, 0, 0, list_val))
        

        #list of various lengths
        list_val =[0,1,2,3,4,7,8,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 7)
        list_val =[0,1,2,3,4,7,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 6)
        list_val =[0,1,2,3,4,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 5)
        list_val =[0,1,2,3,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 4)
        list_val =[0,1,2,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 3)
        list_val =[0,1,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 2)
        list_val =[0,10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 1)
        list_val =[10]
        self.assertEqual(bin_search(10, 0, len(list_val)-1, list_val), 0)
        
        #check empty list
        list_val = []
        self.assertIsNone(bin_search(10, 0 , len(list_val)-1, list_val))
        list_val = []
        self.assertIsNone(bin_search(10, 0 , 0, list_val))



if __name__ == "__main__":
        unittest.main()
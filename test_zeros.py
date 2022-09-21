from unittest import TestCase, main
from nums_array_zeros import move_zeros

class NumZerosTestCase(TestCase):
    def test_1_zero_front(self):
        self.assertEqual(move_zeros([0,0,1,2,3,4]),[1,2,3,4,0,0]) #function call and answer
    
    def test_2_zeros_between(self):
        self.assertEqual(move_zeros([1,0,2,0,3,0,4,0]),[1,2,3,4,0,0,0,0])

    def test_3_all_zeros(self):
        self.assertEqual(move_zeros([0,0,0]),[0,0,0])

    def test_4_no_zeros(self):
        self.assertEqual(move_zeros([1,2,3,4,5]),[1,2,3,4,5])

    def test_5_only_1_zero(self):
        self.assertEqual(move_zeros([1,2,0,3,4,5]),[1,2,3,4,5,0])

    def test_6_three_mid_zeros(self):
        self.assertEqual(move_zeros([1,2,0,0,0,3,4]),[1,2,3,4,0,0,0])
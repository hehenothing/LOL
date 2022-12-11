import unittest
import main
 
class CalcTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(main.add(1, 2), 3)
        
    def test_sub(self):
        self.assertEqual(main.sub(4, 2), 2)
        
    def test_mul(self):
        self.assertEqual(main.mul(2, 5), 10)
        
    def test_div(self):
        self.assertEqual(main.div(8, 4), 2)

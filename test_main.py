import unittest
import main
from circle import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):

    def test_area(self):
        self.assertEqual(main.circle_area(3),pi*3**2)
        self.assertEqual(main.circle_area(1),pi)
        self.assertEqual(main.circle_area(0),0)
        self.assertEqual(main.circle_area(2.5),pi*2.5**2)


    def test_values(self):
        self.assertRaises(ValueError,main.circle_area,-2)
        self.assertRaises(ValueError,main.circle_area,-1)



    def test_types(self):
        self.assertRaises(TypeError, main.circle_area, 5 + 2j)
        self.assertRaises(TypeError, main.circle_area, 'five')
        self.assertRaises(TypeError, main.circle_area, [16, 22])
        self.assertRaises(TypeError, main.circle_area, [42])
        self.assertRaises(TypeError, main.circle_area, True)

import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_calculer_perimetre(self):
        rect_1 = Rectangle(3, 3)
        self.assertEqual(rect_1.calculer_perimetre(), 12)
    def test_calculer_surface(self):
        rect_1 = Rectangle(3, 3)
        self.assertEqual(rect_1.calculer_surface(), 9)

if __name__ == '__main__':
    unittest.main()

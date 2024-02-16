import unittest
from moyenne_liste import calculer_moyenne

class TestCalculerMoyenne(unittest.TestCase):
    def test_moyenne_entiers(self):
        self.assertEqual(calculer_moyenne([1, 2, 3, 4, 5]), 3.0)

    def test_moyenne_decimaux(self):
        self.assertAlmostEqual(calculer_moyenne([1.5, 2.5, 3.5]), 2.5)

    def test_moyenne_negatifs(self):
        self.assertEqual(calculer_moyenne([-1, -2, -3, -4, -5]), -3.0)

    def test_moyenne_vide(self):
        with self.assertRaises(ZeroDivisionError):
            calculer_moyenne([])

if __name__ == '__main__':
    unittest.main()
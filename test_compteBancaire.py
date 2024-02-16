import unittest
from compteBancaire import CompteBancaire

class TestCompteBancaire(unittest.TestCase):

    def test_deposer(self):
        compte = CompteBancaire.__init__(self,100)
        CompteBancaire.deposer(self,100)
        self.assertEqual(CompteBancaire.obtenir_solde(self), 200)

    def test_retirer(self):
        compte = CompteBancaire.__init__(self,200)
        CompteBancaire.retirer(self,100)
        self.assertEqual(CompteBancaire.obtenir_solde(self), 100)

    def test_solde_insuffisant(self):
        compte = CompteBancaire.__init__(self,50)
        with self.assertRaises(ValueError):
            CompteBancaire.retirer(self,100)

if __name__ == '__main__':
    unittest.main()
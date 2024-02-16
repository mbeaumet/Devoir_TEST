import unittest
from somme_liste import somme_liste

class nb_elem(unittest.TestCase):
    def test_list_pleine(self):
        liste=[1,2,3]
        self.assertEqual(somme_liste(liste),6)
    def test_list_pleine_negative(self):
        liste=[-1,-2,-3]
        self.assertEqual(somme_liste(liste),-6)
    def test_list_pleine(self):
        liste=[]
        self.assertEqual(somme_liste(liste),0)
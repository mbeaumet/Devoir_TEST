import unittest
from est_premier import est_premier

class TestEstPremier(unittest.TestCase):

    def test_non_premier(self):
        list_non_premiers=[4,6,10,12]
        for nombres in list_non_premiers:
            self.assertTrue(est_premier(nombres))
    def test_est_premier(self):
        list_premiers=[2,3,5,7,11,13,17,19,23,29]
        for nombres in list_premiers:
            self.assertTrue(est_premier(nombres))

if __name__ == '__main__':
    unittest.main()
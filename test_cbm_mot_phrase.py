import unittest
from cbm_mot_phrase import cbm_mot_phrase

class NbMotPhrase(unittest.TestCase):
    def test_nb_mot(self):
        phrase="Bonjour a tous"
        self.assertEqual(cbm_mot_phrase(phrase),3)

    def test_phrase_vide(self):
        phrase=""
        self.assertEqual(cbm_mot_phrase(phrase),0)

    def test_nb_mot_false(self):
        phrase="Allo"
        self.assertEqual(cbm_mot_phrase(phrase),4)

if __name__ == '__main__':
    unittest.main()
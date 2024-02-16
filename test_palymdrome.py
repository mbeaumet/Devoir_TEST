from palymdrome import est_palindrome
import unittest

class TestEstPalindrome(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(est_palindrome("radar"))
        self.assertFalse(est_palindrome("python"))
 

if __name__ == '__main__':
    unittest.main()

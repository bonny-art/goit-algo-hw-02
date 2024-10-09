import unittest
from palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_true_palindromes(self):
        """Test palindromes that should return True."""
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("Able was I ere I saw Elba"))
        self.assertTrue(is_palindrome("Madam In Eden, I'm Adam"))
        self.assertTrue(is_palindrome("A Santa at NASA"))

    def test_not_palindromes(self):
        """Test non-palindromes that should return False."""
        self.assertFalse(is_palindrome("Python"))
        self.assertFalse(is_palindrome("OpenAI"))

    def test_true_palindromes_with_punctuation(self):
        """Test palindromes with punctuation that should return True."""
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))

    def test_short_palindromes(self):
        """Test short strings, including single characters and empty strings."""
        self.assertTrue(is_palindrome("a"))
        self.assertFalse(is_palindrome("ab"))
        self.assertTrue(is_palindrome(""))

    def test_mixed_upper_lower(self):
        """Test palindromes with mixed uppercase and lowercase letters."""
        self.assertTrue(is_palindrome("Eva, Can I Stab Bats In A Cave?"))
        self.assertTrue(is_palindrome("Mr. Owl Ate My Metal Worm"))

if __name__ == '__main__':
    unittest.main()

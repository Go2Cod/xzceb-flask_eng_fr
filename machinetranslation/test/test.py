import unittest

from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('hello'),'bonjour')
        self.assertEqual(english_to_french('goodbye'),'au revoir')
        # Test None returns empty string
        self.assertNotEqual(english_to_french("None"), '')
        # Test empty string returns empty string
        #self.assertNotEqual(english_to_french(0), 0)

class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('bonjour'),'hello')
        self.assertEqual(french_to_english('au revoir'),'goodbye')
        # Test None returns empty string
        self.assertNotEqual(french_to_english("None"), '')
        # Test empty string returns empty string
        #self.assertNotEqual(french_to_english(0), 0)

if __name__ == "__main__":    
    unittest.main()
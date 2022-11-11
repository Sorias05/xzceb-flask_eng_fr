import unittest

from machinetranslation import translator

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.english_to_french('Hello'), 'Bonjour')
    def test2(self):
        self.assertNotEqual(translator.english_to_french('Bye'), 'Aurevoir')

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.french_to_english('Bonjour'), 'Hello')
    def test2(self):
        self.assertNotEqual(translator.french_to_english('Au revoir'), 'By')

unittest.main()
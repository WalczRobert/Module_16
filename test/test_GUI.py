import unittest

from model.anagram import Anagram
from gui_functions import *


class GUIFunctionsTest(unittest.TestCase):
    def setUp(self):
        self.word_no_anagrams = 'Tiger'
        self.word_with_anagrams = 'computer'
        self.word_with_symbols = 'wor%'
        self.word_with_numbers = 'wor3'
        self.word_with_caps = 'Words'
        self.word_with_no_caps = 'words'
        self.word_with_spaces = "words "
        self.anagram = Anagram(self.word_no_anagrams)

    def tearDown(self):
        del self.anagram

    def test_format_input_with_word(self):
        expected_result = 'omcoputer'
        self.assertEqual(format_input(self.word_with_anagrams), expected_result)

    def test_format_input_with_word_with_caps(self):
        expected_result = 'sdrow'
        self.assertEqual(format_input(self.word_with_caps), expected_result)

    def test_format_input_with_word_with_spaces(self):
        expected_result = 'sdrow'
        self.assertEqual(format_input(self.word_with_spaces), expected_result)


if __name__ == '__main__':
    unittest.main()
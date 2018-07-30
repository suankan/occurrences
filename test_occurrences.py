'''
Test module for occurrences module.
'''

import unittest
from occurrences import find_all_occurrences


class TestFindAllOccurrences(unittest.TestCase):
    '''
    Tests for occurrences module.
    '''

    textToSearch = 'Peter told me that peter the pickle piper piped a' \
        ' pitted pickle before he petered out. Phew!'

    def test_capitalised_pattern(self):
        '''
        Test to find a capitalised string
        '''
        result = find_all_occurrences(self.textToSearch, "Peter")
        self.assertEqual(result, "1, 20, 75")

    def test_non_capitalised_pattern_00(self):
        '''
        Test to find a non capitalised string
        '''
        result = find_all_occurrences(self.textToSearch, "peter")
        self.assertEqual(result, "1, 20, 75")

    def test_non_capitalised_pattern_01(self):
        '''
        One more test to find a non capitalised string
        '''
        result = find_all_occurrences(self.textToSearch, "pick")
        self.assertEqual(result, "30, 58")

    def test_non_capitalised_pattern_02(self):
        '''
        One more test to find a non capitalised string
        '''
        result = find_all_occurrences(self.textToSearch, "pi")
        self.assertEqual(result, "30, 37, 43, 51, 58")

    def test_pattern_non_found_00(self):
        '''
        Test to find a non existing string
        '''
        result = find_all_occurrences(self.textToSearch, "z")
        self.assertEqual(result, "<No Output>")

    def test_pattern_non_found_01(self):
        '''
        One more test to find a non existing string
        '''
        result = find_all_occurrences(self.textToSearch, "Peterz")
        self.assertEqual(result, "<No Output>")


if __name__ == '__main__':
    unittest.main()

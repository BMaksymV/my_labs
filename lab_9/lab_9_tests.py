import unittest
from lab_9 import search_automaton

class TestAutomatonSearch(unittest.TestCase):
    def test_standard_search(self):
        self.assertEqual(search_automaton("AABAACAADAABAABA", "AABA"), [0, 9, 12])

    def test_overlapping_matches(self):
        self.assertEqual(search_automaton("AAAAA", "AA"), [0, 1, 2, 3])

    def test_no_match(self):
        self.assertEqual(search_automaton("HELLO WORLD", "XYZ"), [])

if __name__ == '__main__':
    unittest.main()
import unittest
import os
from lab_5 import flood_fill

class TestFloodFill(unittest.TestCase):

    def setUp(self):
        self.input_filename = 'input.txt'
        self.output_filename = 'output.txt'

    def tearDown(self):
        if os.path.exists(self.output_filename):
            os.remove(self.output_filename)

    def test_flood_fill_main_example(self):

        expected_output = [
            "['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G']",
            "['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'C', 'C', 'C']",
            "['G', 'G', 'G', 'G', 'G', 'G', 'G', 'C', 'C', 'C']",
            "['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'C']",
            "['W', 'R', 'R', 'R', 'R', 'R', 'G', 'C', 'C', 'C']",
            "['W', 'W', 'W', 'R', 'R', 'G', 'G', 'C', 'C', 'C']",
            "['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'C']",
            "['W', 'B', 'B', 'B', 'B', 'R', 'R', 'C', 'C', 'C']",
            "['W', 'B', 'B', 'C', 'B', 'B', 'B', 'B', 'C', 'C']",
            "['W', 'B', 'B', 'C', 'C', 'C', 'C', 'C', 'C', 'C']"
        ]

        flood_fill(self.input_filename, self.output_filename)

        
        with open(self.output_filename, 'r', encoding='utf-8') as f:
            result_lines = [line.strip() for line in f if line.strip()]

        for res_line, exp_line in zip(result_lines, expected_output):
            self.assertEqual(res_line, exp_line)

if __name__ == '__main__':
    unittest.main()
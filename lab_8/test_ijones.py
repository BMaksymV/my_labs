import unittest
import os
import shutil
from ijones import solve 

class TestIndianaJones(unittest.TestCase):

    def run_case(self, in_file, out_file):

        shutil.copy(in_file, 'ijones.in')

        solve()

        with open('ijones.out', 'r') as f:
            result = f.read().strip()

        with open(out_file, 'r') as f:
            expected = f.read().strip()

        self.assertEqual(result, expected)

    def test_example_1(self):
        self.run_case('test1.in', 'test1.out')

    def test_example_2(self):
        self.run_case('test2.in', 'test2.out')

if __name__ == '__main__':
    unittest.main()
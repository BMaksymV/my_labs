import unittest
from lab_7 import read_matrix, prim_alg

class TestPrimFromFile(unittest.TestCase):

    def test_from_file(self):
        matrix = read_matrix("islands.csv")
        self.assertEqual(prim_alg(matrix), 40)


if __name__ == '__main__':
    unittest.main()
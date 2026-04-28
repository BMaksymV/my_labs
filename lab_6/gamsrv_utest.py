import unittest
from gamsrv import minimize, read_input


class TestFromFile(unittest.TestCase):

    def test_example_1(self):
        n, m, clients, graph = read_input("gamsrv.in")
        result = minimize(n, m, clients, graph)
        
        expected = 100
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
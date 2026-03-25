import unittest
from red_black_priority_queue import RedBlackPriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_insert_and_peek(self):
        self.pq.insert("Boy1", 10)
        self.pq.insert("Boy2", 50)
        self.pq.insert("Girl1", 30)

        self.assertEqual(self.pq.peek(), ("Boy2", 50))

    def test_pop(self):
        self.pq.insert("Boy1", 10)
        self.pq.insert("Boy2", 50)
        self.pq.insert("Girl1", 30)

        self.assertEqual(self.pq.pop(), ("Boy2", 50))
        self.assertEqual(self.pq.peek(), ("Girl1", 30))

    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek())
        self.assertIsNone(self.pq.pop())


if __name__ == "__main__":
    unittest.main()
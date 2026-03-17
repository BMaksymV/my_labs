import unittest
from lab_3 import BinaryTreeSuccessor

class TestBinaryTreeSuccessor(unittest.TestCase):

    
    def setUp(self):
        self.root = BinaryTreeSuccessor(10)
        self.root.left = BinaryTreeSuccessor(5)
        self.root.right = BinaryTreeSuccessor(15)
        self.root.left.left = BinaryTreeSuccessor(3)
        self.root.left.right = BinaryTreeSuccessor(7)
        self.root.right.left = BinaryTreeSuccessor(12)
        self.root.right.right = BinaryTreeSuccessor(20)

    def test_standard_case_successor_of_7(self):
        target = self.root.left.right 
        expected_successor = self.root  
        
        self.assertEqual(self.root.find_successor(target), expected_successor)

    def test_root_case_successor_of_10(self):
        target = self.root 
        expected_successor = self.root.right.left 
        
        self.assertEqual(self.root.find_successor(target), expected_successor)

    def test_first_node_successor_of_3(self):
        target = self.root.left.left 
        expected_successor = self.root.left 
        
        self.assertEqual(self.root.find_successor(target), expected_successor)

    def test_edge_case_no_successor_for_20(self):
        target = self.root.right.right
        
        self.assertIsNone(self.root.find_successor(target))

if __name__ == "__main__":
    unittest.main()
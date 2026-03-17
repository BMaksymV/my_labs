class BinaryTreeSuccessor:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def inorder(self, nodes):
        if self.left: 
            self.left.inorder(nodes)
            
        nodes.append(self) 
            
        if self.right: 
            self.right.inorder(nodes)

    def find_successor(self, target_node):
        nodes = []
        self.inorder(nodes)
        
        for i in range(len(nodes) - 1):
            if nodes[i] == target_node:
                return nodes[i + 1]
        return None

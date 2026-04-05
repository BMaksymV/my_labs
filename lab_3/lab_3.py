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
        
        found_target = False
        
        for node in nodes:
            if found_target and node.value > target_node.value:
                return node
            if node == target_node:
                found_target = True
                
        return None

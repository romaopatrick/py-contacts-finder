    
class BNode:
    def __init__(self, value):
        self.value = value
        self.left: BNode | None = None
        self.right: BNode | None = None

class BTree:
    def __init__(self, initial_values = []):
        self.root = None
        [self.insert(v) for v in initial_values]
        
    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)
        
    def _insert_recursive(self, node: BNode, value) -> BNode:
        if not node:
            return BNode(value)
        
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
            return node
        
        node.right = self._insert_recursive(node.right, value)
        return node
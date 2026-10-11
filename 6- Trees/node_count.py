class TreeNode:
    def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


tree_node1 = TreeNode(10)
tree_node1.left = TreeNode(5)
tree_node1.right = TreeNode(20)

tree_node2 = tree_node1.left
tree_node2.left = TreeNode(3)
tree_node2.right = TreeNode(7)

def count(node):
   if node is None:
      return 0
   return 1 + count(node.left) + count(node.right)

print(count(tree_node1))
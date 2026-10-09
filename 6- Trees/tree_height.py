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

def height(node):
   if node is None:
      return -1
   left_height = height(node.left)
   right_height = height(node.right)

   return 1 + max(left_height, right_height)

print(height(tree_node1))
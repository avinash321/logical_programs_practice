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

def find_max(node):
   if node is None:
      return float("-inf")
   left_max = find_max(node.left)
   right_max = find_max(node.right)

   return max(node.data, left_max, right_max)

print(find_max(tree_node1))

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

from collections import deque
def bfs_tree(root):
   if root is None:
      return
   
   queue = deque([root])

   while queue:
      node = queue.popleft()
      print(node.data)
      if node.left:
         queue.append(node.left)
      if node.right:
         queue.append(node.right)

bfs_tree(tree_node1)
   
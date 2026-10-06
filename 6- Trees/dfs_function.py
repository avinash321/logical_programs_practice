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


def dfs(node):
    if node is None:
        return

    print(node.data)
    dfs(node.left)
    dfs(node.right)

dfs(tree_node1)




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating Nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

# Connecting Nodes
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# traversing across nodes
current = head
while current:
    print(current.data)
    current = current.next

def reverse(head):
    previous = None
    current = head
    next_node = current.next
    while current:
      # 1. Save next
      next_node = current.next

      # 2. Reverse the pointer
      current.next = previous

       # 3. Move previous
      previous = current

      # 4. Move current
      current = next_node
    return previous

# traversing across nodes - reverse order
current = reverse(head)
while current:
    print(current.data)
    current = current.next


    

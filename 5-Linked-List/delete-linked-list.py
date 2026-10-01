class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(15)
node3 = Node(20)
node4 = Node(30)

# Connecting Nodes
head = node1
node1.next = node2
node2.next = node3
node3.next = node4

# Deleting
node1.next = node1.next.next

current = head
while current:
    print(current.data)
    current = current.next
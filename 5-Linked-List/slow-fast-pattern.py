class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

# Linking
head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# slow pattern
current = head
while current:
    print(current.data)
    current = current.next

# fast pattern
slow = head
fast = head
slow = slow.next
fast = fast.next.next

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

# Derriving mid value
print(slow.data)
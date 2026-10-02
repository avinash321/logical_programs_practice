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

def find_middle(head):
    slow = head.next
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

print(find_middle(head)) 




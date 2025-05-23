class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#crrating nodes
node1 = Node(23)
node2 = Node(2)
node3 = Node(29)
node4 = Node(20)
        
#connecting nodes

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

#print linked list


current = node1

while current is not None:
    print(current.data,end="->")
    current = current.next
print('None')
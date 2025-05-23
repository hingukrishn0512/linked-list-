#A Linked List is a data structure used to store a sequence of elements, where each element (called a Node) contains:

#Data

#A reference (pointer) to the next node in the list


# A class to represent a node
class Node:
    def __init__(self, data):
        self.data = data  # data value
        self.next = None  # pointer to next node

# A class to represent the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # initially the list is empty

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.next = new_node  # Link last node to new node

    # Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)

ll.display()  # Output: 10 -> 20 -> 30 -> None

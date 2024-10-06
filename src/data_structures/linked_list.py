class Node:
    """
    Node class implementation for singly linked list.
    
    Attributes: data, next
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """
    Implementation of a Singly Linked List class
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a new node with given data to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Display the linked list."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)

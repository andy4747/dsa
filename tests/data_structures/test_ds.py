from src.data_structures.linked_list import SinglyLinkedList

def test_singly_linked_list():
    ll = SinglyLinkedList()
    assert ll.display() == ""
    
    ll.append(1)
    assert ll.display() == "1"
    
    ll.append(2)
    ll.append(3)
    assert ll.display() == "1 -> 2 -> 3"
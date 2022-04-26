# Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node, not necessarily the exact middle) of a singly linked list, given only access to that node.


from linked_list import Node, LinkedList


def delete_middle_node(ll, val):
    if not ll.head:
        return
    current_node = ll.head
    if current_node.value == val:
        return None

    while current_node.next:
        if current_node.next.value == val:
            if current_node.next.next:
                current_node.next = current_node.next.next   
                return
        current_node = current_node.next
        
    return
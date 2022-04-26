# Implement an algorithm to find the kth to last element of a singly linked list.

from linked_list import Node, LinkedList

def return_kth_to_last(ll, k):
    l = []
    if not ll.head:
        return 
    count = 0
    current_node = ll.head
    while count != k:
        if not current_node.next:
            return
        print(count, current_node.value)
        current_node = current_node.next
        count += 1
    while current_node:
        print(count, current_node.value)
        l.append(current_node.value)
        current_node = current_node.next
    return l
# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does not need to appear between the left and right partitions.

def partition(ll, val):
    current_node = ll.head
    end_node = ll.tail

    count = 0
    while current_node:
        print(count, current_node.value)
        count += 1
        next_node = current_node.next
        current_node.next = None
        if current_node.value < val:
            current_node.next = ll.head
            current_node.previous = None
            ll.head = current_node
        else:
            current_node.previous = ll.tail
            ll.tail.next = current_node
            ll.tail = current_node

        if next_node.value == end_node.value:
            return

        current_node = next_node
    
    return

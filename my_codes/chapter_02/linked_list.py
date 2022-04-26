# Python list
#   append(), pop() -> operation complexity is O(1).
#   insert(), remove() -> operation complexity is O(N).
# Linked list
#   operation complexity is O(1).
# http://www.laurentluce.com/posts/python-list-implementation/
# https://realpython.com/linked-lists-python/


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#         self.previous = None

    def __repr__(self):
        return self.value

class NodeDouble:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __repr__(self):
        return self.value


class LinkedList:
    '''usage
    single linked list
    llist = LinkedList(["a", "b", "c", "d", "e"])
    '''
    def __init__(self, nodes=None) -> None:
        self.head = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = node
            for el in nodes:
                node.next = Node(value=el)
                node = node.next
                
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)
    

    def __iter__(self):
        '''iterator
        for node in llist:
            print(node)
        '''
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        '''
        insert at the beginning
        '''
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        '''
        insert at the last
        '''
        if self.head is None:
            self.head = node
            return 
        else: 
            for current_node in self:
                pass
            current_node.next = node

    def insert(self, target_node_value, new_node):
        '''
        insert between two nodes
        '''
        for current_node in self:
            if current_node.value == target_node_value:
                new_node.next = current_node.next
                current_node.next = new_node
                return

    def remove(self, target_node_value):
        '''
        remove an element
        '''
        if self.head == target_node_value:
            self.head = self.head.next
            return
        previous_node = self.head
        for current_node in self:
            if current_node.value == target_node_value:
                previous_node.next = current_node.next
                return
            previous_node = current_node


class LinkedListDouble:
    '''usage
    double linked list
    llist = LinkedList(["a", "b", "c", "d", "e"])
    '''
    def __init__(self, nodes=None) -> None:
        self.head = None
        self.tail = None
        if nodes is not None:
            node = Node(value=nodes.pop(0))
            self.head = self.tail = node
            for el in nodes:
                node.next = Node(value=el)
                node.next.previous = node
                node = node.next
                self.tail = node
                
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append('None')
        return '->'.join(nodes)
    

    def __iter__(self):
        '''iterator
        for node in llist:
            print(node)
        '''
        node = self.head
        while node is not None:
            yield node
            node = node.next

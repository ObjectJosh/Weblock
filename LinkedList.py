from Node import *

class LinkedList:
    # A doubly linked list with no ordering
    def __init__(self, sentinel=None):
        self.sentinel = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self):
        # returns true if linked list is empty
        return self.sentinel.item is None

    def add(self, item):
        # adds an item to the linked list
        current = self.sentinel
        previous = None
        stop = False
        temp = Node(item)
        if self.is_empty():
            self.sentinel = temp
            return None
        while current is not None and not stop:
            previous = current
            current = current.next
        temp.prev = previous
        previous.next = temp
        self.size += 1

    def remove(self, item):
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        current = self.sentinel
        if not self.search(item):
            return False
        if item == current.item and len(self.python_list()) == 1:
            self.sentinel = Node(None)
            return True
        if self.index(item) == 0:
            current = current.next
            current.prev = None
            self.sentinel = current
            return True
        elif self.index(item) == self.size() - 1:
            while current is not None:
                previous = current
                current = current.next
            temp = previous
            previous = temp.prev
            previous.next = None
            return True
        else:
            while current.item != item:
                current = current.next
            left = current.prev
            right = current.next
            left.next = right
            right.prev = left
            return True
        self.size -= 1

    def index(self, item):
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        current = self.sentinel
        if not self.search(item):
            return None
        return self.index_helper(item, current)

    def search(self, item):
        """Searches OrderedList for item, returns True if item is in list, False otherwise"""
        current = self.sentinel
        return self.search_helper(item, current)

    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        current = self.sentinel
        python_list = []
        while current is not None:
            python_list.append(current.item)
            current = current.next
        return python_list

    def python_list_reversed(self):
        """Return a Python list representation of OrderedList, from tail to head, using recursion
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        python_list = self.python_list()
        return self.python_list_reversed_helper(python_list)

    def size(self):
        """Returns number of items in the OrderedList. O(n) is OK"""
        return self.size

    def python_list_reversed_helper(self, list_input):
        length = len(list_input)
        if length <= 1:
            return list_input
        return list_input[length - 1:] + self.python_list_reversed_helper(list_input[:length - 1])

    def size_helper(self, node):
        if node is None:
            return 0
        return 1 + self.size_helper(node.next)

    def index_helper(self, item, node):
        if item == node.item:
            return 0
        return 1 + self.index_helper(item, node.next)

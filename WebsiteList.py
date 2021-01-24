################################
##### Website List Class #######
################################
from Website import *

# acts as a doubly linked list to make it easier to remove and add items, also makes searching easier
class WebsiteList:
    def __init__(self):
        self.sentinel = Website(None, None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self.size = 0

    # checks if the list is empty
    def isEmpty(self):
        """Returns back True if list is empty"""
        return self.sentinel.getName() is None

    # adds an item to the list
    def add(self, website):
        current = self.sentinel
        previous = None
        stop = False
        temp = website
        if self.isEmpty():
            self.sentinel = temp
            return None
        while current is not None and not stop:
            if current.name > website.getName():
                stop = True
            elif current.name == website.getName():
                stop = True
            else:
                previous = current
                current = current.next
        if previous is not None and current is not None:
            temp.prev = previous
            temp.next = current
            previous.next = temp
            current.prev = temp
        elif previous is not None and current is None:
            temp.prev = previous
            previous.next = temp
        elif previous is None and current is not None:
            temp.next = current
            current.prev = temp

    def remove(self, item):
        current = self.sentinel
        if not self.search(item):
            return False
        if item == current.item and len(self.python_list()) == 1:
            self.sentinel = Website(None, None)
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

    def index(self, item):
        current = self.sentinel
        if not self.search(item):
            return None
        return self.index_helper(item, current)


    def python_list(self):
        """Return a Python list representation of OrderedList, from head to tail
        with website links"""
        current = self.sentinel
        python_list = []
        while current is not None:
            python_list.append(current.websiteLink)
            current = current.next
        return python_list

    def size(self):
        """Returns number of items in the OrderedList. O(n) is OK"""
        current = self.sentinel
        return self.size_helper(current)

    def size_helper(self, node):
        if node is None:
            return 0
        return 1 + self.size_helper(node.next)
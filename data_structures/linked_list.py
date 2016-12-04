# -*- coding: utf-8 -*-
"""Implementation of the linked list data structure.

Built upon the implementation in:
    Problem Solving with Algorithms and Data Structures
    By Brad Miller and David Ranum
    <https://interactivepython.org/runestone/static/pythonds/BasicDS/
        ImplementinganUnorderedListLinkedLists.html>
    Copyright 2014 Brad Miller, David Ranum; Licensed under the Creative
    Commons Attribution-NonCommercial-ShareAlike 4.0 International License
    <https://creativecommons.org/licenses/by-nc-sa/4.0/>

Notes:
    Implementation made PEP8 compliant, Python 3 compatible, docstrings added,
    magic methods added, and more cleanly expressed overall.
"""


class Node(object):
    """Holds an item in a linked list."""

    def __init__(self, data):
        self.data = data
        self.next_ = None

    def get_data(self):
        """Get  data value for node."""
        return self.data

    def get_next(self):
        """Get data for the next node."""
        return self.next_

    def set_data(self, new_data):
        """Update data held in this node."""
        self.data = new_data

    def set_next(self, new_next):
        """Update next node data reference."""
        self.next_ = new_next


class LinkedList(object):
    """Implementation of linked list."""

    def __init__(self):
        self.head = None

    def __len__(self):
        return self.size()

    def is_empty(self):
        """Check if list has no head, and therefore, is empty."""
        return not self.head

    def add(self, item):
        """Add item to the list."""
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Traverse the list and return size."""
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        """Traverse the list looking for item."""
        current = self.head
        found = False
        while current and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        """Traverse the list until item is found, then remove it."""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

# -*- coding: utf-8 -*-
"""Implementation of the deque data structure.

Built upon the implementation in:
    Problem Solving with Algorithms and Data Structures
    By Brad Miller and David Ranum
    <https://interactivepython.org/runestone/static/pythonds/BasicDS/
        ImplementingaDequeinPython.html>
    Copyright 2014 Brad Miller, David Ranum; Licensed under the Creative
    Commons Attribution-NonCommercial-ShareAlike 4.0 International License
    <https://creativecommons.org/licenses/by-nc-sa/4.0/>

Notes:
    Implementation made PEP8 compliant, Python 3 compatible, docstrings added,
    magic methods added, and more cleanly expressed overall.
"""


class Deque(object):
    """Implementation of a deque."""

    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def __repr__(self):
        return self.items

    def is_empty(self):
        """Test whether deque is empty."""
        return self.items == []

    def add_front(self, item):
        """Add item to front of deque."""
        self.items.append(item)

    def add_rear(self, item):
        """Add item to rear of deeque."""
        self.items.insert(0, item)

    def remove_front(self):
        """Remove front item from deque."""
        self.items.pop()

    def remove_rear(self):
        """Remove rear item from deque."""
        self.items.pop(0)

    def size(self):
        """Return number of items in deque."""
        return len(self.items)

# -*- coding: utf-8 -*-
"""Implementation of the stack data structure.

Built upon the implementation in:
    Problem Solving with Algorithms and Data Structures
    By Brad Miller and David Ranum
    <https://interactivepython.org/runestone/static/pythonds/BasicDS/
        ImplementingaStackinPython.html>
    Copyright 2014 Brad Miller, David Ranum; Licensed under the Creative
    Commons Attribution-NonCommercial-ShareAlike 4.0 International License
    <https://creativecommons.org/licenses/by-nc-sa/4.0/>

Notes:
    Implementation made PEP8 compliant, Python 3 compatible, docstrings added,
    magic methods added, and more cleanly expressed overall.
"""


class Stack(object):
    """Implementation of a stack in python."""

    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def __repr__(self):
        return self.items

    def size(self):
        """Return number of items in stack."""
        return len(self.items)

    def is_empty(self):
        """Test to see whether the stack is emtpy."""
        return self.items == []

    def push(self, item):
        """Add a new item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove top item from stack."""
        return self.items.pop()

    def peek(self):
        """Return top item from stack without removing it."""
        item_len = len(self.items)
        if item_len > 0:
            return self.items[item_len - 1]
        else:
            return

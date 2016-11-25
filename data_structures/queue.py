# -*- coding: utf-8 -*-
"""Implementation of the queue data structure.

Built upon the implementation in:
    Problem Solving with Algorithms and Data Structures
    By Brad Miller and David Ranum
    <https://interactivepython.org/runestone/static/pythonds/BasicDS/
        ImplementingaQueueinPython.html>
    Copyright 2014 Brad Miller, David Ranum; Licensed under the Creative
    Commons Attribution-NonCommercial-ShareAlike 4.0 International License
    <https://creativecommons.org/licenses/by-nc-sa/4.0/>

Notes:
    Implementation made PEP8 compliant, Python 3 compatible, docstrings added,
    magic methods added, and more cleanly expressed overall.
"""


class Queue(object):
    """Implementation of a queue."""

    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def __repr__(self):
        return self.items

    def is_empty(self):
        """Test to see whether queue is empty."""
        return self.items == []

    def enqueue(self, item):
        """Add new item to rear of queue."""
        return self.items.insert(0, item)

    def dequeue(self):
        """Remove front item from queue."""
        return self.items.pop()

    def size(self):
        """Return number of items in queue."""
        return len(self.items)

# -*- coding: utf-8 -*-
"""Implementation of Binary Search Tree.

Built upon the implementation in:
    Problem Solving with Algorithms and Data Structures
    By Brad Miller and David Ranum <https://interactivepython.org/runestone/
    static/pythonds/Trees/SearchTreeImplementation.html>
    Copyright 2014 Brad Miller, David Ranum; Licensed under the Creative
    Commons Attribution-NonCommercial-ShareAlike 4.0 International License
    <https://creativecommons.org/licenses/by-nc-sa/4.0/>

Notes:
    Implementation made PEP8 compliant, Python 3 compatible, docstrings added,
    and more cleanly expressed overall. Also note that there is a bug in the
    original implementation--some of the methods which should be in the
    TreeNode class were in the BinarySearchTree class, causing delete
    functionality to be broken. Fixed here.
"""


class BinarySearchTree(object):
    """Implementation of Binary Search Tree."""

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        """Return size of tree, defined as number of nodes."""
        return self.size

    def __len__(self):
        """Define length of tree by return value of length method."""
        return self.size

    def __iter__(self):
        """Overload class __iter__ method with __iter__ method of root."""
        return self.root.__iter__()

    def __setitem__(self, key, value):
        """Overload the [] assignment operator with put method."""
        self.put(key, value)

    def __getitem__(self, key):
        """Define __getitem__ method to call get."""
        return self.get(key)

    def __contains__(self, key):
        """Define in operator."""
        return bool(self._get(key, self.root))

    def __delitem__(self, key):
        """Assign del operator to self.delete() method."""
        self.delete(key)

    def put(self, key, val):
        """Insert a news node in the tree."""
        # TODO:
        # A duplicate key will create a new node with the same key value
        # in the right subtree of the node having the original key.
        # The result of this is that the node with the new key will never
        # be found during a search. A better way to handle the insertion
        # of a duplicate key is for the value associated with the new key
        # to replace the old value.

        if self.root:
            # If root exists, search tree for where to put this node
            self._put(key, val, self.root)
        else:
            # otherwise, this node is the root, can be directly inserted
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, current_node):
        """Recursively search tree for a position to place node in."""
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(
                    key, val, parent=current_node
                )
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, val, parent=current_node
                )

    def get(self, key):
        """Return node key from the tree. If no nodes exist, return None"""
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        """Recursively search tree for node to return."""
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def delete(self, key):
        """Delete node from tree."""
        if self.size > 1:
            # We will have to search the tree
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError('Key not in tree')
        elif self.size == 1 and self.root.key == key:
            # Key to remove is only member
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Key not in tree')

    def remove(self, current_node):
        if current_node.is_leaf():  # leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():  # interior
            succ = current_node.find_succesor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:  # this node has only one child:
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(
                        current_node.left_child.key,
                        current_node.left_child.payload,
                        current_node.left_child.right_child
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.replace_node_data(
                        current_node.right_child.payload,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child
                    )


class TreeNode(object):
    """Implementation of Node in Binary Search Tree."""

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def __iter__(self):
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value, left_child=None, right_child=None):
        self.key = key
        self.payload = value
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child:
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_succesor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_succesor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

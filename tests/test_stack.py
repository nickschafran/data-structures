# -*- coding: utf-8 -*-
import unittest
from .context import data_structures


class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = data_structures.Stack()

    def test_stack_instantiate(self):
        self.assertIsInstance(self.stack, data_structures.Stack)

    def test_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())

    def test_stack_push(self):
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())
        self.assertEqual(len(self.stack), 1)

    def test_stack_pop(self):
        self.stack.push(1)
        self.assertEqual(len(self.stack), 1)
        self.stack.pop()
        self.assertEqual(len(self.stack), 0)

    def test_size(self):
        self.assertEqual(self.stack.size(), 0)
        self.stack.push(1)
        self.assertEqual(self.stack.size(), 1)

    def test_peek(self):
        self.assertIsNone(self.stack.peek())
        self.stack.push(1)
        self.assertEqual(self.stack.peek(), 1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)

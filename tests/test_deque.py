# -*- coding: utf-8 -*-
import unittest
from .context import data_structures


class TestDeque(unittest.TestCase):

    def setUp(self):
        self.deque = data_structures.Deque()

    def test_deque_instantiate(self):
        self.assertIsInstance(self.deque, data_structures.Deque)

    def test__repr__(self):
        self.assertIsInstance(self.deque.__repr__(), list)

    def test_is_empty(self):
        self.assertTrue(self.deque.is_empty())

    def test_add_front(self):
        self.assertEqual(len(self.deque), 0)
        self.deque.add_front(1)
        self.assertEqual(len(self.deque), 1)

    def test_add_rear(self):
        self.assertEqual(len(self.deque), 0)
        self.deque.add_rear(1)
        self.assertEqual(len(self.deque), 1)

    def test_remove_front(self):
        self.assertEqual(len(self.deque), 0)
        self.deque.add_front(1)
        self.assertEqual(len(self.deque), 1)
        self.deque.remove_front()
        self.assertEqual(len(self.deque), 0)

    def test_remove_rear(self):
        self.assertEqual(len(self.deque), 0)
        self.deque.add_rear(1)
        self.assertEqual(len(self.deque), 1)
        self.deque.remove_rear()
        self.assertEqual(len(self.deque), 0)

    def test_size(self):
        self.assertEqual(self.deque.size(), 0)
        self.deque.add_front(1)
        self.assertEqual(self.deque.size(), 1)


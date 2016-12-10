# -*- coding: utf-8 -*-
import unittest
from .context import data_structures


class TestNode(unittest.TestCase):

    def setUp(self):
        self.node = data_structures.linked_list.Node('test')

    def test_node_instantiate(self):
        self.assertIsInstance(self.node, data_structures.linked_list.Node)

    def test_get_data(self):
        self.assertEqual(self.node.data, self.node.get_data())

    def test_get_next(self):
        self.assertEqual(self.node.next_, self.node.get_next())

    def set_data(self):
        self.assertEqual(self.node.data, 'test')
        self.node.set_data('test_2')
        self.assertEqual(self.node.data, 'test_2')

    def set_next(self):
        self.assertIsNone(self.next_)
        self.node.set_next('new_next')
        self.node.assertEqual(self.node.next_, 'new_next')

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = data_structures.LinkedList()

    def test_list_instantiate(self):
        self.assertIsInstance(self.linked_list, data_structures.LinkedList)

    def test_len(self):
        self.linked_list.add(42)
        self.linked_list.add(77)
        self.linked_list.add(17)
        self.linked_list.add(93)
        self.linked_list.add(26)
        self.linked_list.add(54)
        self.assertEqual(len(self.linked_list), 6)
        self.assertEqual(len(self.linked_list), self.linked_list.size())


    def test_is_empty(self):
        self.assertTrue(self.linked_list.is_empty())
        self.linked_list.add(42)
        self.assertFalse(self.linked_list.is_empty())

    def test_add(self):
        self.linked_list.add(42)
        self.assertIsNotNone(self.linked_list.head)

    def test_search(self):
        self.assertFalse(self.linked_list.search(42))
        self.linked_list.add(42)
        self.linked_list.add(93)
        self.linked_list.add(26)
        self.linked_list.add(54)
        self.assertTrue(self.linked_list.search(42))

    def test_remove(self):
        self.linked_list.add(42)
        self.assertTrue(self.linked_list.search(42))
        self.linked_list.remove(42)
        self.assertFalse(self.linked_list.search(42))

    def test_remove_longer_list(self):
        self.linked_list.add(77)
        self.linked_list.add(17)
        self.linked_list.add(42)
        self.linked_list.add(93)
        self.linked_list.add(26)
        self.linked_list.add(54)
        self.assertTrue(self.linked_list.search(42))
        self.linked_list.remove(42)
        self.assertFalse(self.linked_list.search(42))

    def test_set_next(self):
        self.linked_list.add(42)
        self.linked_list.head.set_data(43)
        self.assertIsNotNone(self.linked_list.head)

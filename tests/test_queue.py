# -*- coding: utf-8 -*-
import unittest
from .context import data_structures


class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = data_structures.Queue()

    def test_queue_instantiate(self):
        self.assertIsInstance(self.queue, data_structures.Queue)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(len(self.queue), 1)

    def test_dequeue(self):
        self.queue.enqueue(1)
        self.assertEqual(len(self.queue), 1)
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())

    def test_size(self):
        self.assertEqual(len(self.queue), 0)
        self.queue.enqueue(1)
        self.assertEqual(len(self.queue), 1)

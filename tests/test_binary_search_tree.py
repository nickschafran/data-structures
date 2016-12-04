# -*- coding: utf-8 -*-
import unittest
from .context import data_structures


class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.bst = data_structures.BinarySearchTree()

    def test_bst_instantiate(self):
        self.assertIsInstance(self.bst, data_structures.BinarySearchTree)

    def test_bst_length(self):
        self.bst[4] = 1
        self.bst[2] = 3
        self.bst[3] = 5
        expected_len = 3
        self.assertEqual(len(self.bst), expected_len)
        self.assertEqual(self.bst.length(), expected_len)

    def test_put(self):
        # Probably a poorly designed test; the idea is
        # to make sure __setitem__() method works
        self.assertIsInstance(self.bst, data_structures.BinarySearchTree)

    def test_get_exists(self):
        self.bst[4] = 1
        self.assertEqual(self.bst[4], 1)

    def test_get_nonexisting(self):
        self.assertIsNone(self.bst[50])

    def test_get_empty_tree(self):
        self.assertIsNone(self.bst[3])

    def test_contains(self):
        # This seems like a weird use of __contains__?
        self.bst[4] = 1
        self.assertTrue(4 in self.bst)

    def test_delete_node_bst_of_one(self):
        self.bst[1] = 'Short-Lived'
        self.assertTrue(1 in self.bst)
        del self.bst[1]
        self.assertFalse(1 in self.bst)

    def test_delete_node_bst_of_many(self):
        self.bst[1] = 'Short-Lived'
        self.bst[2] = 'Shorter-Lived'
        self.assertTrue(2 in self.bst)
        del self.bst[2]
        self.assertFalse(2 in self.bst)
        with self.assertRaises(KeyError):
            del self.bst[2]

    def test_delete_node_bst_of_none(self):
        with self.assertRaises(KeyError):
            del self.bst[1]

    def test_delete_node_both_children(self):
        self.bst[1] = 'a'
        self.bst[2] = 'a'
        self.bst[0] = 'a'
        self.assertTrue(self.bst.root.has_both_children())
        del self.bst[1]
        self.assertFalse(1 in self.bst)

    def test_delete_left_child_node(self):
        self.bst[1] = 'a'
        self.bst[2] = 'a'
        self.bst[0] = 'a'
        left_child = self.bst._get(0, self.bst.root)
        self.assertTrue(left_child.is_left_child())
        del self.bst[0]
        self.assertFalse(0 in self.bst)

    def test_delete_right_child_node(self):
        self.bst[1] = 'a'
        self.bst[2] = 'a'
        self.bst[0] = 'a'
        right_child = self.bst._get(2, self.bst.root)
        self.assertTrue(right_child.is_right_child())
        del self.bst[2]
        self.assertFalse(2 in self.bst)

    def test_iter_yields_correct_key(self):
        self.bst[1] = 'a'
        self.bst[2] = 'a'
        self.bst[0] = 'a'
        for i in self.bst:
            self.assertIsInstance(i, int)

class TestTreeNode(unittest.TestCase):

    TreeNode = data_structures.binary_search_tree.TreeNode

    def setUp(self):
        self.mynode = self.TreeNode(1, 'test')

    def test_tree_node_instantiate(self):
        self.assertIsInstance(self.mynode, self.TreeNode)

    def test_has_right_child(self):
        self.assertFalse(self.mynode.has_right_child())
        self.mynode.right_child = 2
        self.assertTrue(self.mynode.has_right_child())

    def test_has_left_child(self):
        self.assertFalse(self.mynode.has_left_child())
        self.mynode.left_child = 2
        self.assertTrue(self.mynode.has_left_child())

    # These two are tested elsewhere:
    @unittest.skip('Even though this is covered elsewhere, should have a test')
    def test_is_left_child(self):
        pass

    @unittest.skip('Even though this is covered elsewhere, should have a test')
    def test_is_right_child(self):
        pass

    def test_is_root(self):
        self.assertTrue(self.mynode.is_root())

    def test_is_leaf(self):
        self.assertTrue(self.mynode.is_leaf())

    def test_has_any_children(self):
        self.assertFalse(self.mynode.has_any_children())

    def test_has_both_children(self):
        self.assertFalse(self.mynode.has_both_children())

    def test_replace_node_data(self):
        self.mynode.replace_node_data(1, 'b')
        self.assertTrue(self.mynode.payload, 'b')

    def test_splice_out_with_right_child(self):
        self.mynode.parent = self.TreeNode(0, 'test')
        self.mynode.right_child = self.TreeNode(2, 'test')
        self.mynode.splice_out()
        self.assertTrue(bool(self.mynode.has_any_children()))

    def test_splice_out_with_right_child(self):
        self.mynode.parent = self.TreeNode(0, 'test')
        self.mynode.left_child = self.TreeNode(0, 'test')
        self.mynode.splice_out()
        self.assertTrue(bool(self.mynode.has_any_children()))


if __name__ == '__main__':
    unittest.main()

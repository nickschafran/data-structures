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

    def test_delete_bst_of_one(self):
        self.bst[1] = 'Short-Lived'
        self.assertTrue(1 in self.bst)
        del self.bst[1]
        self.assertFalse(1 in self.bst)

    def test_delete_bst_of_many(self):
        self.bst[1] = 'Short-Lived'
        self.bst[2] = 'Shorter-Lived'
        self.assertTrue(2 in self.bst)
        del self.bst[2]
        self.assertFalse(2 in self.bst)
        with self.assertRaises(KeyError):
            del self.bst[2]

    def test_delete_bst_of_none(self):
        with self.assertRaises(KeyError):
            del self.bst[1]

if __name__ == '__main__':
    unittest.main()

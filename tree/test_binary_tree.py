import numpy as np
import typing
import unittest

from node import Node
from binary_tree import *


class TreeGenerator(object):

    @staticmethod
    def generate_structure(numbers: np.array, index: int) -> typing.Optional[Node]:
        if index < len(numbers):
            left = TreeGenerator.generate_structure(numbers, index*2+1)
            right = TreeGenerator.generate_structure(numbers, index*2+2)
            return Node(numbers[index], left, right)
        else:
            return None

    @staticmethod
    def tree_height_1() -> typing.Tuple[Node, np.array, int]:
        rep = np.array([0, 1])
        return TreeGenerator.generate_structure(rep, 0), rep, 1

    @staticmethod
    def tree_height_2() -> typing.Tuple[Node, np.array, int]:
        rep = np.array([0, 1, 2, 3, 4, 5, 6])
        return TreeGenerator.generate_structure(rep, 0), rep, 4

    @staticmethod
    def tree_height_3() -> typing.Tuple[Node, np.array, int]:
        rep = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return TreeGenerator.generate_structure(rep, 0), rep, 5

    @staticmethod
    def tree_height_4() -> typing.Tuple[Node, np.array, int]:
        rep = np.array([13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
        return TreeGenerator.generate_structure(rep, 0), rep, 7

    @staticmethod
    def bst_height_2() -> typing.Tuple[Node, np.array, int, int]:
        rep = np.array([3, 1, 5, 0, 2, 4, 6])
        return TreeGenerator.generate_structure(rep, 0), rep, 2, 4

    @staticmethod
    def bst_slides() -> typing.Tuple[Node, np.array, int, int]:
        rep = np.array([60, 20, 80, 10, 40, 70, 100, 1, 15, 30, 45, 65, 71, 99])
        return TreeGenerator.generate_structure(rep, 0), rep, 45, 65

    @staticmethod
    def all_bt_cases():
        return [
            TreeGenerator.tree_height_1(),
            TreeGenerator.tree_height_2(),
            TreeGenerator.tree_height_3(),
            TreeGenerator.tree_height_4()
        ]

    @staticmethod
    def all_bst_cases():
        return [
            TreeGenerator.bst_height_2(),
            TreeGenerator.bst_slides()
        ]


class TestTreeFunctions(unittest.TestCase):

    def test_count_leafs(self):
        for tree, _, num_leafs in TreeGenerator.all_bt_cases():
            counted_leafs = count_leafs(tree)
            self.assertEqual(num_leafs, counted_leafs)

    def test_get_height(self):
        for tree, rep, _ in TreeGenerator.all_bt_cases():
            # adjustment 16/02: aligned with definition of the book
            # (tree of just the root node has height 0, etc)
            height = int(np.ceil(np.log2(len(rep)+1))) - 1
            counted_height = get_height(tree)
            self.assertEqual(height, counted_height)

    def test_get_highest_value(self):
        for tree, rep, _ in TreeGenerator.all_bt_cases():
            max_value = np.max(rep)
            max_encountered = get_highest_value(tree)
            self.assertEqual(max_value, max_encountered)

    def test_get_greatest_smaller_value(self):
        for tree, _, gsv, _ in TreeGenerator.all_bst_cases():
            node = get_greatest_smaller_value(tree)
            self.assertEqual(gsv, node.info)

    def test_get_smallest_greater_value(self):
        for tree, _, _, sgv in TreeGenerator.all_bst_cases():
            node = get_smallest_greater_value(tree)
            self.assertEqual(sgv, node.info)

    def test_is_binary_search_tree(self):
        for tree, _, _ in TreeGenerator.all_bt_cases():
            is_bst = is_binary_search_tree(tree)
            self.assertFalse(is_bst)

        for tree, _, _, _ in TreeGenerator.all_bst_cases():
            is_bst = is_binary_search_tree(tree)
            self.assertTrue(is_bst)

    def test_search(self):
        for tree, rep, _, _ in TreeGenerator.all_bst_cases():
            for value in range(20):
                in_rep = value in list(rep)
                parent, child = search(tree, value)
                self.assertEqual(in_rep, child is not None)

    def test_add(self):
        for tree, rep, _, _ in TreeGenerator.all_bst_cases():
            for value in range(20):
                in_rep = value in list(rep)
                result = add(tree, value)
                self.assertNotEqual(in_rep, result)
                # careful, this test relies on the proper functioning of
                # search / is_binary_search_tree
                parent, child = search(tree, value)
                self.assertFalse(child is None)
                self.assertTrue(is_binary_search_tree(tree))

    def test_delete(self):
        for value in range(20):
            for tree, rep, _, _ in TreeGenerator.all_bst_cases():
                in_rep = value in list(rep)
                result, tree = remove(tree, value)
                self.assertEqual(in_rep, result)
                # careful, this test relies on the proper functioning of
                # search / is_binary_search_tree
                parent, child = search(tree, value)
                self.assertTrue(child is None)
                self.assertTrue(is_binary_search_tree(tree))
    
    def test_delete_manual(self):
        # original tree
        ll = Node(0, None, None)
        lr = Node(2, None, None)
        p = Node(1, ll, lr)

        #lll = Node(3.2, None, None)
        #lrr = Node(4.2, None, None)
        l = Node(4, None, None)
        r = Node(6, None, None)
        rp = Node(5, l,r)
        root = Node(3, p, rp)

        remove(root, value=3)
        
        # Solution tree root2 (of removing value 3)
        ll2 = Node(0, None, None)
        lr2 = Node(2, None, None)
        p2 = Node(1, ll2, lr2)

        #lll = Node(3.2, None, None)
        #lrr = Node(4.2, None, None)
        r2 = Node(6, None, None)
        rp2 = Node(5, None, r2)
        root2 = Node(4, p2, rp2)

        def tree_to_string(root: Node, tree_chars):
            if root is not None:
                tree_to_string(root.left, tree_chars)
                tree_chars.append(root.info) 
                tree_to_string(root.right, tree_chars)
            return np.array(tree_chars)
        
        tc_original = tree_to_string(root2, [])
        tc_removed = tree_to_string(root, [])

        self.assertTrue(np.all(tc_original == tc_removed))


        # original tree
        ll = Node(0, None, None)
        lr = Node(2, None, None)
        p = Node(1, ll, lr)
        l = Node(4, None, None)
        r = Node(6, None, None)
        rp = Node(5, l,r)
        root = Node(3, p, rp)

        remove(root, value=5)
        
        # Solution tree root2 (of removing value 3)
        ll2 = Node(0, None, None)
        lr2 = Node(2, None, None)
        p2 = Node(1, ll2, lr2)

        l2 = Node(4, None, None)
        r2 = Node(6, l2, None)
        root2 = Node(3, p2, r2)

        tc_original = tree_to_string(root2, [])
        tc_removed = tree_to_string(root, [])

        self.assertTrue(np.all(tc_original == tc_removed))

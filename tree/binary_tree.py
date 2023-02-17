import numpy as np
import typing

from node import Node
from binary_tree_visualization import visualize_tree


def count_leafs(root: Node) -> int:
    """
    Counts the number of leafs in a binary tree. Recursive function.

    :param root: The root of the (sub)tree
    :return: the number of leafs
    """
    
    if not root.left and not root.right:
        # If node is leaf, return 1
        return 1

    # Traverse subtree
    n_leaves_in_subtree = 0
    if root.left:
        n_leaves_in_subtree += count_leafs(root.left)
    if root.right:        
        n_leaves_in_subtree += count_leafs(root.right)
    
    return n_leaves_in_subtree


def get_height(root: Node) -> int:
    """
    Determines the height of a binary tree. Recursive function.

    :param root: The root of the (sub)tree
    :return: the height of the (sub)tree
    """
    # FIXME:
    if not root:
        return 0
    
    height_left = get_height(root.left)
    height_right = get_height(root.right)
    
    return max(height_left, height_right) + 1


def get_highest_value(root: Node) -> int:
    """
    Gets the highest value out of a binary tree (not a binary search tree!!)
    Recursive function.

    :param root: The root of the (sub)tree
    :return: the highest value within this (sub)tree
    """

    if not root.left and not root.right:
        return root.info

    value_left = 0
    value_right = 0
    if root.left:
        value_left = get_highest_value(root.left)
    if root.right:
        value_right = get_highest_value(root.right)
    return max(root.info, value_left, value_right)


def get_greatest_smaller_value(root: Node) -> Node:
    """
    Returns the node with the greatest value smaller than the root.
    You can assume that this is a binary search tree. Also, you can
    assume that this function will only be used if such smaller values
    exists. Hint: This function is not recursive. Think of the binary 
    search tree property

    :param root: The root of the (sub)tree
    :return: the Node with the greatest value smaller than the root
    """

    value = root.left

    while True:
        if value.info >= root.info or not value.right:
            # Value is higher than root, or node has no right child
            break
        value = value.right

    return value


def get_smallest_greater_value(root: Node) -> Node:
    """
    Returns the node with the smallest value greater than the root.
    You can assume that this is a binary search tree. Also, you can
    assume that this function will only be used if such greater values
    exists. Hint: This function is not recursive. Think of the binary 
    search tree property

    :param root: The root of the (sub)tree
    :return: the Node with the smallest value greater than the root
    """

    value = root.right
    
    while True:
        if value.info <= root.info or not value.right:
            # Value is smaller than root, or node has no left child
            break
        value = value.left

    return value


def is_binary_search_tree(root: Node) -> bool:
    """
    Returns whether the tree is a valid binary search tree. Hint:
    Recursive function. You can under some assumptions make use of
    get_smallest_greater_value and get_greatest_smaller_value.

    :param root: The root of the (sub)tree
    :return: true iff it is a valid binary search tree
    """

    if not root:
        return True

    if root.left and root.left.info > root.info:
        return False

    if root.right and root.right.info < root.info:
        return False
    
    # Recursively check child nodes
    if not is_binary_search_tree(root.left) or not is_binary_search_tree(root.right):
        return False
        
    return True


def search(root: Node, value: int) -> typing.Tuple[typing.Optional[Node], typing.Optional[Node]]:
    """
    Returns a Tuple with the following two items:
     - the parent of the node with a certain value
     - the node with a certain value
    Note that having access to the parent will prove useful
    other functions, such as adding and removing.

    If the binary search tree does not contain the value, return
    the parent of the node where it should have been
    placed, and a None value.

    :param root: The root of the (sub)tree
    :return: tuple of the nodes as described above
    """
    
    parent = root
    while root and root.info != value:
        parent = root
        if value < root.info:
            root = root.left
        elif value > root.info:
            root = root.right  
        else:
            root = None

    return parent, root


def add(root: Node, value: int) -> bool:
    """
    Adds a new node to the binary search tree, respecting the condition that
    for each node all values in the left sub-tree are smaller than its value,
    and all values in the right subtree are greater than its value.
    Only adds the node with the value, if it does not exist yet in the tree.

    :param root: the root of the (sub)tree
    :param value: the value to be added
    :return: true upon success, false upon failure
    """

    parent, found = search(root, value)
    if found:
        return False
    if value > parent.info:
        parent.right = Node(value, None, None)
    else:
        parent.left = Node(value, None, None)
    
    return True


def remove(root: Node, value: int) -> typing.Tuple[bool, typing.Optional[Node]]:
    """
    Removes a node from the binary search tree, respecting the condition that
    for each node all values in the left sub-tree are smaller than its value,
    and all values in the right subtree are greater than its value.
    Only removes the node with the value, if it does exist in the tree.

    :param root: the root of the (sub)tree
    :param value: the value to be deleted
    :return: a Tuple consisting of
      - a boolean of whether the value was found and has been deleted
      - the root node of the new tree
    """

    # TODO: Implement this function

    raise NotImplementedError()

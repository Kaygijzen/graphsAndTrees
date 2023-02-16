import numpy as np
import typing

from node import Node

############################################################################
# This file contains code to visualize trees. You do not need to 
# understand this code. You can call visualize_tree(root: Node)
# to obtain a nice visualization of the given tree. 
# A more basic visualization function that prints trees in a less
# nice manner is given by visualize_tree(root: Node, type: str, depth: int)
############################################################################

# def visualize_tree(root: Node, type: str, depth: int) -> None:
#     print('%s%s> %s' % ('--' * depth, type, root.info))
#     if root is None:
#         return
#     if root.left is not None:
#         visualize_tree(root.left, 'L', depth + 1)
#     if root.right is not None:
#         visualize_tree(root.right, 'R', depth + 1)

def num_digits(n: int):
    """
    Counts the number of digits of an integer

    :param n: The integer to analyze
    """
    if n == 0:
        return 1
    d = (n < 0) # Account for the minus sign
    n = np.abs(n)
    d += int(np.ceil(np.log10(n+0.1)))
    return d

def preorder_traversal(root: Node) -> dict:
    """
    Traverses the tree in preorder creating a dictionary with the nodes
    organized per level. It also stores the position of the node in the 
    corresponding level.

    :param root: The root of the (sub)tree
    :return: A dictionary where keys are levels and values are a lists of tuples 
             containing the value of a node and its position in the level.
    """    
    tree = {}
    node = root
    level = 0
    position = 0
    parent_stack = []
    while(node or len(parent_stack) > 0):
        if(node):
            if tree.get(level) is None:
                tree[level] = []
            tree[level].append((node.info, position))
            parent_stack.append((node, level, position))
            node = node.left
            position = position * 2
            level = level + 1
        else:
            parent, parent_level, parent_position = parent_stack.pop()
            node = parent.right
            level = parent_level + 1
            position = parent_position * 2 + 1
    return tree

def visualize_tree(root: Node) -> None:
    """
    Prints a visualization of the tree with connector lines

    :param root: The root of the (sub)tree
    """
    tree_preorder = preorder_traversal(root)
    nlevels = len(tree_preorder.items())
    for row, nodes in tree_preorder.items():
        level_inv = nlevels - row
        # Is the width of the space at the begining of each line.
        # Between 2 consevutive values in a level there are 2 * space_width spaces
        space_width = pow(2, level_inv)
        connector_line = ''
        # We start the line with spaces. The 1 is for better alignment
        number_line = ' ' * (space_width + 1)
        prev_position = 0
        for i, (value, position) in enumerate(nodes):
            # We substract as many spaces as digits in the first value of the row
            if position == 0:
                number_line = number_line[:-num_digits(value)]
            # We add spaces between values, accounting also for missing values
            number_line += ' ' * (space_width * (position - prev_position) * 2 - num_digits(value))
            number_line += str(value)
            # We add spaces to the connector line in case of missing values
            if  position - prev_position > 1 or (i == 0 and position != 0):
                connector_line += ' ' * space_width * ((position - prev_position - 1 + (i == 0 and position != 0)) * 2)
            # We add the connections with different alignment for left and right children
            if position % 2:
                connector_line += '¯' * (space_width - 1)
                connector_line += '\\'
                connector_line += ' ' * space_width
            else:
                connector_line += ' ' * space_width                    
                connector_line += '/'
                connector_line += '¯' * (space_width - 1)
            prev_position = position
        if row != 0:
            print(connector_line)
        print(number_line)
    print('\n')
    return
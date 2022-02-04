from itertools import count


class Node:
	def __init__(self, value = 0, right = None, left = None) -> None:
		self.value = value
		self.left = left
		self.right = right


def is_unival_tree_rec(node):
    if not node: 
        return True, 0
        
    is_unival_tree_left, count_left = is_unival_tree_rec(node.left)  
    is_unival_tree_right, count_right = is_unival_tree_rec(node.right)
    total_count = count_left + count_right

    if ( is_unival_tree_left and is_unival_tree_right and 
         (not node.left or node.left.value == node.value) and
         (not node.right or node.right.value == node.value)):
            return True, total_count + 1
    else:
        return False, total_count

def is_unival_tree(node):
    return is_unival_tree_rec(node)[1]

assert is_unival_tree(None) == 0

assert is_unival_tree(
	Node(0)
) == 1

assert is_unival_tree(
	Node(
		0,
		Node(1),
	)
) == 1

assert is_unival_tree(
	Node(
		0,
		Node(0),
		Node(0),
	)
) == 3

assert is_unival_tree(
	Node(
		0,
		Node(
            1,
            Node(0),
            Node(1),
        ),
		Node(
            1,
            Node(1),
            Node(1),
        ),
	)
) == 5

assert is_unival_tree(
	Node(
		0,
		Node(
            0,
            Node(0),
            Node(0),
        ),
		Node(
            0,
            Node(0),
            Node(0),
        ),
	)
) == 7
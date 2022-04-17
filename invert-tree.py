
from logging import root


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.root = None
        self.left = left
        self.right = right

def invert_tree(root):
    if root == None: return
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    

def inOrder(node):
    if (node == None):
        return
    print(node.val, end = " ")
    inOrder(node.left)
    inOrder(node.right)

root = Node("a", Node("b", Node("d"), Node("e")), Node("c", Node("f")))
original = Node("a", Node("b", Node("d"), Node("e")), Node("c", Node("f")))

# inOrder(root)
print("mirror tree: ")
invert_tree(root)
inOrder(root)

print("\nnormal tree: ")
invert_tree(root)
inOrder(root)






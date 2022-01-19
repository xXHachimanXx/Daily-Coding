class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Transform Node object into array
def serialize(node):
    # Serialize and store val in current context
    val = node.val

    # Serialize and store node.left in current context
    if node.left:
        left = serialize(node.left)
    else:
        left = None
    
    # Serialize and store node.left in current context
    if node.right:
        right = serialize(node.right)
    else:
        right = None

    # Return all atributes stored in current context
    return [val, left, right]

# Transform array into Node object
def deserialize(array):
    # Deserialize and store val in current context
    val = array[0]
    
    # Serialize and store node.left in current context
    if array[1]:
        left = deserialize(array[1])
    else:
        left = None
    
    # Serialize and store node.right in current context
    if array[2]:
        right = deserialize(array[2])
    else:
        right = None

    # Return a object with all atributes stored in current context
    return Node(val, left, right)

node = Node('root', Node('left', Node('left.left')), Node('right')) 
array = serialize(node)
print(array)
assert deserialize(serialize(node)).left.left.val == 'left.left'

"""
Considering that both serialize and deserialize run through all the tree
generated, it can be said that these algorithms has:

Time complexity = O(2n) = O(n)
Space complexity = O(n)
"""

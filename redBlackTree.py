black = 0
red = 1

class RBTreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.color = red

def setColor(node, color):
    node.color = color
    return node

def color(node):
    if not node:
        return black
    return node.color

def isRed(node):
    return color(node) == red

def rotateLeft(head):
    node = head.right
    head.right = node.left
    node.left = head
    node.color = head.color
    head.color = red
    return node

def rotateRight(head):
    node = head.left
    head.left = node.right
    node.right = head
    node.color = head.color
    head.color = red
    return node

def flipColor(node):
    node.left.color = black
    node.right.color = black
    node.color = red
    return node

def insert(node, value):
    if not node:
        return RBTreeNode(value)
    if value >= node.value:
        node.right = insert(node.right, value)
    else:
        node.left = insert(node.left, value)

    if isRed(node.right) and not isRed(node.left):
        node = rotateLeft(node)
    if isRed(node.left) and isRed(node.left.left):
        node = rotateRight(node)
    if isRed(node.left) and isRed(node.right):
        node = flipColor(node)
    return node

def lookup(node, value, parent = None):
    if value < node.value:
        if node.left is None:
            return None, None
        return lookup(node.left, value, node)
    elif value > node.value:
        if node.right is None:
            return None, None
        return lookup(node.right, value, node)
    else:
        #Not greater than or less than -- you found it!
        return node, parent

def height(node):
    if not node:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)

def printNode(node, indent):
    if not node:
        return
    print " " * indent,
    (v, c) = node.value
    print v, "(black)" if c == 0 else "(red)"
    printNode(node.left, indent + 4)
    printNode(node.right, indent + 4)

def test():
    c = xrange(0, 32768)
    tree = None
    for i in c:
        tree = insert(tree, i)
    insert(tree, 201)
    node, parent = lookup(tree, 201)
    print node.value
    test()

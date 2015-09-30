import math

BLACK = 0
RED = 1

class RBTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.color = RED


def setColor(n, c):
    n.color = c
    return n


def color(n):
    if not n:
        return BLACK
    return n.color


def isRed(n):
    return color(n) == RED


def search(self, val, x = None):
    if None == x:
        x 



def rotateLeft(h):
    x = h.right
    h.right = x.left
    x.left = h
    x.color = h.color
    h.color = RED
    return x


def rotateRight(h):
    x = h.left
    h.left = x.right
    x.right = h
    x.color = h.color
    h.color = RED
    return x


def flipColor(n):
    n.left.color = BLACK
    n.right.color = BLACK
    n.color = RED
    return n


def insert(n, v):
    if not n:
        return RBTreeNode(v)
    if v >= n.val:
        n.right = insert(n.right, v)
    else:
        n.left = insert(n.left, v)

    if isRed(n.right) and not isRed(n.left):
        n = rotateLeft(n)
    if isRed(n.left) and isRed(n.left.left):
        n = rotateRight(n)
    if isRed(n.left) and isRed(n.right):
        n = flipColor(n)
    return n

def lookup(node, val, parent = None):
    if val < node.val:
        if node.left is None:
            return None, None
        return lookup(node.left, val, node)
    elif val > node.val:
        if node.right is None:
            return None, None 
        return lookup(node.right, val, node)
    else:
        #Not greater than or less than -- you found it!
        return node, parent


def height(n):
    if not n:
        return 0

    h1 = height(n.left)
    h2 = height(n.right)
    return 1 + max(h1, h2)


def printNode(n, indent):
    if not n:
        return
    print " " * indent,
    (v, c) = n.val
    print v, "(BLACK)" if c == 0 else "(RED)"
    printNode(n.left, indent + 4)
    printNode(n.right, indent + 4)


def test():
    c = xrange(0, 32768)
    tree = None
    for i in c:
        tree = insert(tree, i)
    insert(tree, 201)
    node, parent = lookup(tree, 201)
    print node.val
if __name__ == "__main__":
    test()
class BSTNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BST:
    def __init__(self):
        self.root = None





one = BSTNode(20)
two = BSTNode(10)
three = BSTNode(30)

tree = BST()
tree.root = one
one.left = two
one.right = three


def printinorder(root):
    if root:
        printinorder(root.left)
        print(root.data)
        printinorder(root.right)

printinorder(tree.root)
# current = tree.root
# while current.left is not None and current.right is not None:

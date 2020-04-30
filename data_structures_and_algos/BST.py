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



def insertinorder(root, node):
    if root is None:
        root = node

    if node.data < root.data:
        if root.left is None:
            root.left = node
        else:
            insertinorder(root.left, node)

    if node.data > root.data:
        if root.right is None:
            root.right = node
        else:
            insertinorder(root.right, node)


insertinorder(tree.root, BSTNode(50))

insertinorder(tree.root, BSTNode(30))
insertinorder(tree.root, BSTNode(70))
insertinorder(tree.root, BSTNode(10))
insertinorder(tree.root, BSTNode(40))
insertinorder(tree.root, BSTNode(60))
insertinorder(tree.root, BSTNode(80))

printinorder(tree.root)

# not included root condition yet
def deleteinorder(root, val):
    if root.left is not None and root.left.data == val:
        pointer = root.left.right
        root.left = root.left.left
        root.left.right = pointer
    elif root.left is not None and root.right.data == val:
        root.right = root.right.right
    if val < root.data:
        if root.left is not None:
            deleteinorder(root.left, val)
    if val > root.data:
        if root.right is not None:
            deleteinorder(root.right, val)

print("\n")
deleteinorder(tree.root, 50)
printinorder(tree.root)

def heighttree(root):
    if root is None:
        return 0
    height = left = right = 0
    lroot = rroot = root
    while lroot.left is not None:
        left += 1
        lroot = lroot.left
    while rroot.right is not None:
        right += 1
        rroot = rroot.right
    if left > right:
        height = left + 1
    else:
        height = right + 1

    return height


print(heighttree(tree.root))





# current = tree.root
# while current.left is not None and current.right is not None:

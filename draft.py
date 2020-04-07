class Node:

    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right.parent = parent

    def __str__(self):
        return str(self.data)


class AVLNode(Node):
    def __init__(self, data=None, left=None, right=None, parent=None, balance=0):
        Node.__init__(self, data, left, right, parent)
        self.balance = balance

    def __str__(self):
        return f"{self.data}({self.balance})"


# przechodzenie ddrzewa binarnego

def btree_inorder(top):
    if top is None:
        return []
    order = []
    order.extend(btree_inorder(top.left))
    order.append(top.data)
    order.extend(btree_inorder(top.right))
    return order


def btree_preorder(top):
    if top is None:
        return []
    order = []
    order.append(top.data)
    order.extend(btree_preorder(top.left))
    order.extend(btree_preorder(top.right))
    return order


def btree_postorder(top):
    if top is None:
        return []
    order = []
    order.extend(btree_inorder(top.left))
    order.extend(btree_inorder(top.right))
    order.append(top.data)
    return order



# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)

    # A function to do postorder tree traversal


def printPostorder(root):
    if root:
        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),

    # A function to do preorder tree traversal


def printPreorder(root):
    if root:
        # First print the data of node
        print(root.val),

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)

    # Driver code


root = Node(0)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)

print("\nInorder traversal of binary tree is")
printInorder(root)

print("\nPostorder traversal of binary tree is")
printPostorder(root)


# wysokosc drzewa
def btree_height(top):
    if top is None:
        return 0
    left = btree_height(top.left)
    right = btree_height(top.right)
    return 1 + max(left, right)


# najmniejszy klucz
def bst_find_min(top):
    if top is None:
        raise ValueError("empty tree")
    while top.left:
        top = top.left
    return top


# najwiekszy klucz
def bst_find_max(top):
    if top is None:
        raise ValueError("empty tree")
    while top.right:
        top = top.right
    return top


# usuwanie elementu z drzewa
def bst_transplant(root, first, second):  # zwraca(root,second)
    # Zastepowanie poddrzewa first przez poddrzewo second.
    # Nie ma tu aktualizacji second.left i second.right.
    if first.parent is None:
        root = second
        if root:
            root.parent = None
        return root, second
    elif first == first.parent.left:
        first.parent.left = second
    else:
        first.parent.right = second
    if second:  # second moze byc None
        second.parent = first.parent
    return root, second


def bts_delete(root, node):
    # zwraca root i wezel, ktory przesunie sie na miejsce node
    if root is None or node is None:
        return root, None
    if node.left is None:
        return bst_transplant(root, node, node.right)
    elif node.right is None:
        return bst_transplant(root, node, node.left)
    else:  # node.left i node.right niepuste
        y = bst_find_min(node.right)
        if y.parent != node:
            root, _ = bst_transplant(root, y, y.right)
            y.right = node.right
            if y.right:
                y.right.parent = y
        root, _ = bst_transplant(root, node, y)
        y.left = node.left
        y.left.parent = y
        return root, y


# rotacja w prawo w bst
def rotate_right(root, top):
    if top.left is None:  # n i e ma r o t a c j i
        return root, top
    node = top.left
    top.left = node.right
    if node.right:
        node.right.parent = top
    node.parent = top.parent
    if top.parent is None:
        root = node  # top byl korzeniem
    elif top == top.parent.right:
        top.parent.right = node
    else:
        top.parent.left = node
    node.right = top
    top.parent = node
    return root, node


# rotacja w lewo w bst
def rotate_left(root, top):
    if top.right is None:  # nie ma rotacji
        return root, top
    node = top.right
    top.right = node.left
    if node.left:
        node.left.parent = top
    node.parent = top.parent
    if top.parent is None:
        root = node  # top byl korzeniem
    elif top == top.parent.left:
        top.parent.left = node
    else:
        top.parrent.right = node
    node.left = top
    top.parent = node
    return root, node


# algorytm DSW
from math import pow, floor, log

def bst_create_backbone(root, top):
    parent = top
    left_child = None
    while parent:
        left_child = parent.left
        if left_child:
            root, _ = rotate_right(root, parent)
            parent = left_child
        else:
            parent = parent.right
    return root


def make_rotations(root, x):
    p = root
    for i in range(x):
        if p:
            root. _ = rotate_left(root, p)
            if p.parent:
                p = p.parent.right
    return root


def bst_create_perfect_tree(root, n):
    root = bst_create_backbone(root, root)
    m = int(pow(2, floor(log(n+1, 2))) - 1)
    root = make_rotations(root, n-m)
    while m> 1 :
        m = m // 2  # jesli chcemy iterowac w make rotations po m,
        # to m musi byc calkowite
        root = make_rotations(root, m)
    return root













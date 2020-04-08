from ngen import *

HEAD = -1


class Node:
    def __init__(self, nodeValue):
        self.val = nodeValue
        self.left = None
        self.right = None

    def __repr__(self):
        return f"\x1b[1m{self.val}\x1b[0m[\x1b[31m{str(self.left)}\x1b[0m] \x1b[1m{self.val}\x1b[0m[\x1b[32m{str(self.right)}\x1b[0m]"


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, new):
        if not self.root:
            self.root = Node(value)
        else:
            node = self.root
            parent = None
            while node:
                parent = node
                node = node.left if new.val < node.val else node.right

            if new.val < parent.val:
                parent.left = new
                parent.left.parent = parent
            else:
                parent.right = new
                parent.right.parent = parent

    def height(self, _from):
        if _from is None:
            return 0
        left, right = self.height(_from.left), self.height(_from.right)
        return 1 + max(left, right)

    def min(self, _from):
        head = _from
        while head.left:
            head = head.left
        return head

    def max(self, _from):
        head = _from
        while head.right:
            head = head.right
        return head

    def find(self, nodeKey):
        head = self.root
        while head:
            print(head)
            if nodeKey == head.val:
                return head
            if nodeKey < head.val:
                head = head.left
            elif nodeKey > head.val:
                head = head.right
        return None

    def pop(self, nodeKey):
        pass

    def preorder(self, node):
        order = []
        if node:
            order.append(node.val)
            order.extend(self.preorder(node.left))
            order.extend(self.preorder(node.right))
        return order

    def inorder(self, node):
        order = []
        if node:
            order.extend(self.inorder(node.left))
            order.append(node.val)
            order.extend(self.inorder(node.right))
        return order

    def postorder(self, node):
        order = []
        if node:
            order.extend(self.postorder(node.left))
            order.extend(self.postorder(node.right))
            order.append(node.val)
        return order


class BSTTree(Tree):
    def __init__(self, src):
        self.root, src = Node(src[0]), [Node(val) for val in src[1:]]
        [self.insert(n) for n in src]


class AVLTree(Tree):
    """docstring for AVLTree."""

    def __init__(self, src):
        super(AVLTree, self).__init__()
        if src:
            self.root = self.__construct(sorted(src))

    def __construct(self, data) -> Node:
        if data:
            root = Node(data.pop((len(data) - 1) // 2))
            root.left = self.__construct(data[:len(data) // 2])
            root.right = self.__construct(data[len(data) // 2:])
            if root.left:
                root.left.parent = root
            if root.right:
                root.right.parent = root
            return root


testdata = sorted(rand(10))
print(sorted(testdata))
akacja = AVLTree(testdata)

print(
    f"testdata :: {testdata}\n",
    akacja.root,
    '\n',
    "height :: ", akacja.height(_from=akacja.root), '\n',
    "min :: ", akacja.min(_from=akacja.root).val, '\n',
    "max :: ", akacja.max(_from=akacja.root).val, '\n',
    f"preorder :: {akacja.preorder(akacja.root)}\n",
    f"inorder :: {akacja.inorder(akacja.root)}\n",
    f"postorder :: {akacja.postorder(akacja.root)}\n"

)

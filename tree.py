from ngen import *
from math import pow, floor, log

HEAD = -1


class Node:
    def __init__(self, nodeValue):
        self.val = nodeValue
        self.left = None
        self.right = None
        self.parent = None

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

    def path_to_min(self):
        if not self.root:
            return []
        alist = [self.root.val]
        node = self.root
        while node.left:
            alist.append(node.left.val)
            node = node.left
        return alist

    def path_to_max(self):
        if not self.root:
            return []
        alist = [self.root.val]
        node = self.root
        while node.right:
            alist.append(node.right.val)
            node = node.right
        return alist

    def find(self, nodeKey):
        head = self.root
        while head:
            print(head.val)
            if nodeKey == head.val:
                return head
            if nodeKey < head.val:
                head = head.left
            elif nodeKey > head.val:
                head = head.right
        return head

    def remove(self, node):
        if not node:
            return None
        node_parent = node.parent
        child_num = bool(node.left) + bool(node.right)
        if child_num == 0:
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = None
                else:
                    node_parent.right = None
            else:
                self.root = None

        elif child_num == 1:
            child = node.left if node.left else node.right
            if node_parent:
                if node_parent.left == node:
                    node_parent.left = child
                else:
                    node_parent.right = child
            else:
                self.root = child
            child.parent = node_parent

        elif child_num == 2:
            new_node = node.right
            while new_node.left:
                new_node = new_node.left
            node.value = new_node.val
            self.remove(new_node)

    def delete(self):
        n = input("Ile kluczy chcesz usunąć?")
        try:
            n = int(n)
        except ValueError:
            print("Należy podać liczbę")
            self.delete()
        n = int(n)
        if n == 0:
            return None
        keys = []
        print("Podaj klucze:")
        for i in range(n):
            try:
                keys.append(int(input(f"{i + 1}. ")))
            except ValueError:
                print("Należy podać liczbę")
                self.delete()
        for key in keys:
            x = self.find(key)  # zwraca caly korzen pod tym elementem
            if x:
                print("key", x)
                self.remove(x)
            else:
                print("Nie ma takiego klucza")
                self.delete()

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

    def delete_by_postorder(self, node):
        arr = self.postorder(node)
        print("arr: ", arr)
        for el in arr:
            x = self.find(el)
            self.remove(x)
            print("deleted: ", el)
            print("node: ", node)

    def __rotate_right(self, top: Node):
        node = top.left
        top.left = node.right
        if node.right:
            node.right.parent = top
        node.parent = top.parent
        if not top.parent:
            self.root = node
        elif top == top.parent.right:
            top.parent.right = node
        else:
            top.parent.left = node
        node.right = top
        top.parent = node

    def __rotate_left(self, top: Node):
        node = top.right
        top.right = node.left

        if node.left:
            node.left.parent = top

        node.parent = top.parent
        if not top.parent:
            self.root = node
        elif top is top.parent.left:
            top.parent.left = node
        elif top is top.parent.right:
            top.parent.right = node
        node.left = top
        top.parent = node

    def __make_rotations(self, x):
        top = self.root
        for i in range(x):
            if top:
                self.__rotate_left(top)
                if top.parent:
                    top = top.parent.right

    def __create_spine(self):
        parent = self.root
        while parent:
            left = parent.left
            if left:
                self.__rotate_right(parent)
                parent = left
            else:
                parent = parent.right

    def balance(self):
        root, n = self.root, self.count()
        m = int(pow(2, floor(log(n + 1, 2))) - 1)

        self.__create_spine()
        self.__make_rotations(n - m)
        while m > 1:
            m = m // 2
            self.__make_rotations(m)


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
# akacja = BSTTree(testdata)
print(
    f"testdata :: {testdata}\n",
    akacja.root,
    '\n',
    "height :: ", akacja.height(_from=akacja.root), '\n',
    "min :: ", akacja.min(_from=akacja.root).val, '\n',
    "max :: ", akacja.max(_from=akacja.root).val, '\n',
    "path to min :: ", akacja.path_to_min(), '\n',
    "path to max :: ", akacja.path_to_max(), '\n',
    f"preorder :: {akacja.preorder(akacja.root)}\n",
    f"inorder :: {akacja.inorder(akacja.root)}\n",
    f"postorder :: {akacja.postorder(akacja.root)}\n"
    f"postorder delete :: {akacja.delete_by_postorder(akacja.root)}\n"

)


# usuwanie wybranych elementow:
akacja.delete()
print("Drzewo po usunieciu: ", akacja.root)

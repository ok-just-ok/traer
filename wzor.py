from math import pow, floor, log
from random import sample
from typing import List, Union

class Node(object):
    def __init__(self, value):
        self.right = self.left = self.parent = None
        self.value = value

class AVLNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.height = 0

class Tree(object):
    def __init__(self):
        self.root = None

    # region [Methods][Nodes | Modify]
    # region [Nodes][Print | Height | Count | Paths]
    # region [Print][Pre Order | In Order]
    # region [Pre Order]
    def print_pre_order(self):
        print('PreOrder')
        print(*map(lambda x: x.value, self.pre_order()))

    def pre_order(self):
        return self.__pre_order(self.root)

    def __pre_order(self, node: Node):
        if node:
            yield node
            yield from self.__pre_order(node.left)
            yield from self.__pre_order(node.right)

    # endregion
    # region [In Order]
    def print_in_order(self):
        print('InOrder')
        print(*map(lambda x: x.value, self.in_order()))

    def in_order(self):
        return self.__in_order(self.root)

    def __in_order(self, node: Node):
        if node:
            yield from self.__in_order(node.left)
            yield node
            yield from self.__in_order(node.right)

    # endregion
    # region [Post Order]
    def print_post_order(self):
        print('PostOrder')
        print(*map(lambda x: x.value, self.post_order()))

    def post_order(self):
        return self.__in_order(self.root)

    def __post_order(self, node: Node):
        if node:
            yield from self.__post_order(node.left)
            yield from self.__post_order(node.right)
            yield node

    # endregion
    # endregion
    # region [Height]
    def find_height(self) -> int:
        return self.__find_height(self.root) if self.root else 0

    def __find_height(self, node: Node) -> int:
        if not node: return 0
        return max([self.__find_height(node.left), self.__find_height(node.right)])+1

# endregion
    # region [Count]
    def count(self):
        return self.__count(self.root)

    def __count(self, root):
        if not root: return 0
        return self.__count(root.left) + 1 + self.__count(root.right)

    # endregion
    # region [Paths]
    # region [Find]
    def find(self, value: int) -> Node:
        return self.__find(self.root, value)

    def __find(self, node: Node, value: int) -> Node:
        if value == node.value:
            return node
        if value < node.value and node.left:
            return self.__find(node.left, value)
        elif value > node.value and node.right:
            return self.__find(node.right, value)

    # endregion
    # region [Min]
    def find_min_path(self) -> list:
        if not self.root:
            return []

        lst = [self.root]
        node = self.root
        while node.left:
            lst.append(node.left)
            node = node.left
        return lst

    # endregion
    # region [Max]
    def find_max_path(self) -> list:
        if not self.root:
            return []

        lst = [self.root]
        node = self.root
        while node.right:
            lst.append(node.right)
            node = node.right
        return lst

    # endregion
# endregion
    # endregion
    # region [Modify][Balance | Insert | Remove | Delete]
    # region [Balance][Rotation | Spine | Balance]
    # region [Rotation]
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

    # endregion
    # region [Spine]
    def __create_spine(self):
        parent = self.root
        while parent:
            left = parent.left
            if left:
                self.__rotate_right(parent)
                parent = left
            else:
                parent = parent.right

    # endregion
    # region [Balance]
    def balance(self):
        root, n = self.root, self.count()
        m = int(pow(2, floor(log(n + 1, 2))) - 1)

        self.__create_spine()
        self.__make_rotations(n - m)
        while m > 1:
            m = m // 2
            self.__make_rotations(m)

    # endregion
    # endregion
    # region [Insert]
    def insert(self, value: int):
        if not self.root: self.root = Node(value)
        else:
            node = self.root
            parent = None
            while node:
                parent = node
                node = node.left if value < node.value else node.right

            if value < parent.value:
                parent.left = Node(value)
                parent.left.parent = parent
            else:
                parent.right = Node(value)
                parent.right.parent = parent

    # endregion
    # region [Remove]
    def remove(self, value):
        self.__remove_node(self.find(value))

    def __remove_node(self, node):
        if not node: return None

        node_parent = node.parent
        child_num: int = bool(node.left)+bool(node.right)
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

            node.value = new_node.value
            self.__remove_node(new_node)

# endregion
    # region [Delete]
    def delete(self):
        for node in self.post_order():
            self.__remove_node(node)
    # endregion
    # endregion
    # endregion

class BST(Tree):
    def __init__(self, data=None):
        super().__init__()
        if data: self.__construct(data)

    # region [Constructor]
    def __construct(self, data: List[int]):
        [self.insert(val) for val in data]

    # endregion


class AVL(BST):
    def __init__(self, data):
        super().__init__()
        if data: self.root = self.__construct(sorted(data))

    def __construct(self, data) -> Node:
        if data:
            root = Node(data.pop((len(data) - 1) // 2))
            root.left = self.__construct(data[:len(data) // 2])
            root.right = self.__construct(data[len(data) // 2:])
            if root.left: root.left.parent = root
            if root.right: root.right.parent = root
            return root


# region [List Generators]

def ascending(n: int) -> List[int]:
    return list(range(1, n+1))

def descending(n: int) -> List[int]:
    return list(range(n, 0, -1))

def random(n: int) -> List[int]:
    return sample(list(range(1, n+1)), n)

# endregion

ar = AVL(random(10))
ar.print_pre_order()
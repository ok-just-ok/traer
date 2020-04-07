HEAD = -1


class Node:
    def __init__(self, nodeValue):
        self.val = nodeValue
        self.left = None
        self.right = None

    def __repr__(self):
        return f"\x1b[1m{self.val}\x1b[0m[\x1b[31m{str(self.left)}\x1b[0m] \x1b[1m{self.val}\x1b[0m[\x1b[32m{str(self.right)}\x1b[0m]"


class Tree:
    def __init__(self, src):
        self.root, src = Node(src[0]), [Node(val) for val in src[1:]]
        [self.insert(n, self.root) for n in src]

    def insert(self, tail, head):
        if tail.val < head.val:
            if not head.left:
                head.left = tail
                head.left.up = head
            else:
                self.insert(tail, head.left)
        else:
            if not head.right:
                head.right = tail
                head.right.up = head
            else:
                self.insert(tail, head.right)

    def height(self, _from):
        if _from is None:
            return 0
        left, right = self.height(_from.left), self.height(_from.right)
        return 1 + max(left, right)

    def min(self):
        head = self.root
        while head.left:
            head = head.left
        return head

    def max(self):
        head = self.root
        while head.right:
            head = head.right
        return head


testdata = __import__('ngen').rand(10)
akacja = Tree(testdata)
print(sorted(testdata))

print(
    akacja.root,
    '\n',
    "height :: ", akacja.height(_from=akacja.root), '\n',
    "min :: ", akacja.min(), '\n',
    "max :: ", akacja.max(), '\n',
)

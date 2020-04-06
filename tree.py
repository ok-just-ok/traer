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
        print(self.root, src)

        for n in src:
            self.insert(n, self.root)
            print("hello")

    def insert(self, tail, head):
        if tail.val < head.val:
            if not head.left:
                head.left = tail
            else:
                self.insert(tail, head.left)
        else:
            if not head.right:
                head.right = tail
            else:
                self.insert(tail, head.right)


testdata = __import__('ngen').rand(10)
akacja = Tree(testdata)

print(
    akacja.root
)

import time

from ngen import *
from tree import BSTTree, AVLTree

__import__('sys').setrecursionlimit(20000)


def tester(constructor):
    testValues = []
    testRanges = sorted([int(10 * 5 ** (i / 2)) for i in range(10)])
    testRanges = [10, 100, 500, 1000, 2500, 5000, 7000, 9000, 12000]

    for r in testRanges:

        testData = test_data(r)

        start = time.time()

        akacja = constructor(testData)

        created = time.time()

        sprout = akacja.min(_from=akacja.root)

        sprouted = time.time()

        log = akacja.inorder(akacja.root)

        logged = time.time()

        print(f"\n\x1b[1m{r}\x1b[0m")
        print(f"created   {(created-start)}")
        print(f"sprouted  {(sprouted-created)}")
        print(f"logged    {(logged-sprouted)}")


tester(
    constructor=BSTTree
)

import time

from ngen import *
from tree import BSTTree, AVLTree

__import__('sys').setrecursionlimit(20000)


def tester(constructor):
    loggedMemo = []
    createdMemo = []
    sproutedMemo = []
    balancedMemo = []
    testRanges = [10, 100, 500, 1000, 2500, 5000, 7000, 9000, 12000, 12500]
    testRanges = [10, 1000, 10000, 100000, 125000,
                  250000, 375000, 500000, 750000, 1000000]

    for r in testRanges:

        testData = test_data(r)

        start = time.time()

        akacja = constructor(testData)
        # print(akacja.root, file=__import__('sys').stderr)

        created = time.time()

        sprout = akacja.min(_from=akacja.root)

        sprouted = time.time()

        log = akacja.inorder(akacja.root)

        logged = time.time()

        balance = akacja.balance()

        balanced = time.time()

        createdMemo.append(str(created - start))
        sproutedMemo.append(str(sprouted - created))
        loggedMemo.append(str(logged - sprouted))
        balancedMemo.append(str(balanced - logged))

    print("tested N;", '; '.join([str(x) for x in testRanges]))
    print("create;", '; '.join(createdMemo))
    print("min finding;", '; '.join(sproutedMemo))
    print("postorder display;", '; '.join(loggedMemo))
    print("balancing;", '; '.join(balancedMemo))


tester(
    constructor=AVLTree
)

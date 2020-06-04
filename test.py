import time

from ngen import *
from tree import BSTTree, AVLTree

__import__('sys').setrecursionlimit(20000)


# def tester(constructor):
#     loggedMemo = []
#     createdMemo = []
#     sproutedMemo = []
#     balancedMemo = []
#     testRanges = [10, 100, 250, 500, 750, 1000, 2500, 5000, 7500, 10000, 20000]
#     # testRanges = [10, 1000, 10000, 100000, 125000,
#     #               250000, 375000, 500000, 750000, 1000000]
#
#     for r in testRanges:
#
#         testData = test_data(r)
#
#         start = time.time()
#
#         akacja = constructor(testData)
#         # print(akacja.root, file=__import__('sys').stderr)
#
#         created = time.time()
#
#         sprout = akacja.min(_from=akacja.root)
#
#         sprouted = time.time()
#
#         log = akacja.inorder(akacja.root)
#
#         logged = time.time()
#
#         balance = akacja.balance()
#
#         balanced = time.time()
#
#         createdMemo.append(str(created - start))
#         sproutedMemo.append(str(sprouted - created))
#         loggedMemo.append(str(logged - sprouted))
#         balancedMemo.append(str(balanced - logged))
#
#     print("tested N;", '; '.join([str(x) for x in testRanges]))
#     print("create;", '; '.join(createdMemo))
#     print("min finding;", '; '.join(sproutedMemo))
#     print("postorder display;", '; '.join(loggedMemo))
#     print("balancing;", '; '.join(balancedMemo))
#
#
# tester(
#     constructor=BSTTree
# )

drzefo = AVLTree(reversed(sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 12, 23, 34, 45, 56, 67,
                                  78, 89, 90, 13, 24, 35, 46, 57, 68, 79, 80, 123, 234, 345, 456, 567, 678, 789, 890])))

print(drzefo.preorder(drzefo.root), drzefo.height(_from=drzefo.root))

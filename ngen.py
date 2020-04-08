from random import *


def rand(n):
    return [randint(1, 100) for i in range(n)]


def test_data(n):
    tab = rand(1)
    for i in range(1, n):
        tab.append(tab[i - 1] + randint(1, 10))
    return tab[::-1]

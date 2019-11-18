import itertools as it
import time

import numpy as np
from math import sqrt


UNDECIDED = -1
NO_DIAGONAL = 0
BR_TL = 1
BL_TR = 2
BOARD_DIM = 5

start_time = time.time()


def cell_representation(cell):
    if cell == BR_TL:
        return '\\'
    if cell == BL_TR:
        return '/'
    if cell == NO_DIAGONAL:
        return 'O'


def print_board(result, n):
    for i in range(len(result)):
        if i % n == 0:
            print()
        print(cell_representation(result[i]), end='\t')
    print()


def can_be_extended(result, n):
    k = len(result) - 1
    current_cell = result[k]

    if has_left(k, n):
        left_cell = result[left(k)]
        if NO_DIAGONAL != left_cell and current_cell != NO_DIAGONAL and left_cell != current_cell:
            return False

    if has_top(k, n):
        top_cell = result[top(k, n)]
        if NO_DIAGONAL != top_cell and NO_DIAGONAL != current_cell and top_cell != current_cell:
            return False

    if has_top_left(k, n):
        top_left_cell = result[top_left(k, n)]
        if top_left_cell == current_cell == BR_TL:
            return False

    if has_top_right(k, n):
        top_right_cell = result[top_right(k, n)]
        if top_right_cell == current_cell == BL_TR:
            return False

    return True


def count_diags(result):
    return len(list(it.filterfalse(lambda x: x == 0, result)))


def extend(result, n, l):
    diags = count_diags(result)
    if len(result) == n ** 2 and diags == l:
        print_board(result, n)
        elapsed_time = time.time() - start_time
        print('elapsed time: ', "%.2f" % elapsed_time)
        exit()
    if len(result) < n ** 2:
        for x in [BR_TL, BL_TR, NO_DIAGONAL]:
            result.append(x)
            if x == NO_DIAGONAL or can_be_extended(result, n):
                extend(result, n, l)
            result.pop()


def has_left(k, n):
    return k > 0 and k % n > 0


def left(k):
    return k - 1


def has_top(k, n):
    return k - n >= 0


def top(k, n):
    return k - n


def has_top_left(k, n):
    return has_left(k, n) and has_top(k, n)


def top_left(k, n):
    return left(top(k, n))


def has_top_right(k, n):
    return k > 0 and k % n < (n - 1) and has_top(k, n)


def top_right(k, n):
    return top(k, n) + 1


extend([], 5, 16)

import itertools as it


def can_extend(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


def solve(perm, n):
    if len(perm) == n:
        print(perm)
        return

    for k in range(n):
        if k not in perm:
            perm.append(k)
            if can_extend(perm):
                solve(perm, n)
            perm.pop()


solve([], 20)

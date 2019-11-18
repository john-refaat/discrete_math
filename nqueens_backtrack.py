def can_extend(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True


solutions = []


def extract(perm, n):
    if len(perm) == n:
        print(perm)
        solutions.append(perm)
        # return
        # exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)
            if can_extend(perm):
                extract(perm, n)
            perm.pop()


extract([], 8)
print(len(solutions))

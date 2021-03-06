def multiradix_recursive(M, i):
    if i < 0:
        yield []
    else:
        for a in multiradix_recursive(M, i - 1):
            for x in range(M[i]):
                yield a + [x]


def gen_all(M):
    return multiradix_recursive(M, len(M) - 1)

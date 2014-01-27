__author__ = 'sophiahernandez'
# -------
# imports
# -------

import sys


# ------------
# collatz_read
# ------------


def collatz_read(r):
    """
    r is a  reader
    returns an generator that iterates over a sequence of lists of ints of length 2
    for s in r :
        l = s.split()
        b = int(l[0])
        e = int(l[1])
        yield [b, e]
    for s in r :
        yield map(int, s.split())
    """
    return (map(int, s.split()) for s in r)

# ------------
# collatz_eval
# ------------


def collatz_eval((i, j)):
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    # <your code>
    v = 1
    if i > j:
        t = i
        i = j
        j = t
    if j/2 > i:
        i = j/2
    for x in range(i, j+1):
        m = helper(x)
        if m > v:
            v = m
    assert v > 0
    return v


_cache = {1: 1}


def helper(i):
    """
    i is the int to find the cycle length recursively
    return int  cycle length

    """
    if i in _cache:
        return _cache[i]
    elif i % 2:
        _cache[i] = helper(3*i/2 + 1) + 2
        return _cache[i]
    else:
        return helper(i / 2) + 1

# -------------
# collatz_print
# -------------


def collatz_print(w, (i, j), v):
    """
    prints the values of i, j, and v
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------


def collatz_solve(r, w):
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for t in collatz_read(r):
        v = collatz_eval(t)
        collatz_print(w, t, v)


# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)
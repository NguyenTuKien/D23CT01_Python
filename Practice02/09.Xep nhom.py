from sys import stdin
from bisect import bisect_left

def max_group(a, k):
    a.sort()
    n = len(a)
    s = 0
    prefix = [0] * (n + 1)
    for i, x in enumerate(a, 1):
        s += x
        prefix[i] = s
    hi = s // k
    lo = 0
    while lo < hi:
        mid = (lo + hi + 1) // 2
        pos = bisect_left(a, mid)
        total = prefix[pos] + mid * (n - pos)
        if total >= mid * k:
            lo = mid
        else:
            hi = mid - 1
    return lo

def ints():
    for line in stdin:
        for num in line.split():
            yield int(num)

def main():
    it = ints()
    for _ in range(int(next(it))):
        n = next(it)
        k = next(it)
        a = [next(it) for _ in range(n)]
        print(max_group(a, k))

if __name__ == "__main__":
    main()
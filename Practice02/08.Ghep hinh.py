from sys import stdin, stdout
from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def V(a, b, i):
    return i * (a - 2 * i) * (b - 2 * i)

def big(a, b):
    arr = []
    for i in range(1, min(a, b) // 2):
        arr.append(V(a, b, i))
    arr.sort(reverse=True)
    return arr[:3]

if __name__ == "__main__":
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        a, b, x, y, z, l, r = map(int, [next(it) for _ in range(7)])
        v = big(a, b)
        for i in range(x, r + 1, v[0]):
            if i % v[1] == y and i % v[2] == z:
                k = i
                break
        if k < l:
            com = lcm(v[0], lcm(v[1], v[2]))
            d = (l - k) // com
            if d * com + k < l:
                d += 1
            print(k + d * com)
        else:
            print(k)
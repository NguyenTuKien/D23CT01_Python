from sys import stdin, stdout

def count_at_most(K, arr):
    if K < 0:
        return 0
    res = 0
    s = 0
    l = 0
    for r, v in enumerate(arr):
        s += v
        while s > K:
            s -= arr[l]
            l += 1
        res += (r - l + 1)
    return res

def solve_case(n, m, k, rows_bytes):
    if n <= m:
        H, W = n, m
        mat = [[1 if c == 49 else 0 for c in rows_bytes[i]] for i in range(n)]
    else:
        H, W = m, n
        mat = [[0] * W for _ in range(H)]
        for i in range(n):
            rb = rows_bytes[i]
            for j in range(m):
                if rb[j] == 49:
                    mat[j][i] = 1

    ans = 0
    col_sums = [0] * W
    for top in range(H):
        for j in range(W):
            col_sums[j] = 0
        for bottom in range(top, H):
            rowb = mat[bottom]
            for j in range(W):
                col_sums[j] += rowb[j]
            ans += count_at_most(k, col_sums) - count_at_most(k - 1, col_sums)
    return ans

def main():
    data = stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it)); m = int(next(it)); k = int(next(it))
        rows = [next(it) for _ in range(n)] 
        out.append(str(solve_case(n, m, k, rows)))
    stdout.write("\n".join(out))

if __name__ == "__main__":
    main()

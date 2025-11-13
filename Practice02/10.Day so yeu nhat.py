import sys

INF = 1e30

def build_upper_inc(slopes, intercepts):
    hull_k = []
    hull_b = []
    starts = []
    for k, b in zip(slopes, intercepts):
        if not hull_k:
            hull_k.append(k)
            hull_b.append(b)
            starts.append(-INF)
            continue

        while True:
            k1, b1 = hull_k[-1], hull_b[-1]
            x_int = (b1 - b) / (k - k1)

            if x_int <= starts[-1]:
                hull_k.pop()
                hull_b.pop()
                starts.pop()
                if not hull_k:
                    hull_k.append(k)
                    hull_b.append(b)
                    starts.append(-INF)
                    break
            else:
                hull_k.append(k)
                hull_b.append(b)
                starts.append(x_int)
                break

    return hull_k, hull_b, starts


def eval_hull(hull_k, hull_b, starts, x, ptr):
    n = len(hull_k)
    while ptr + 1 < n and starts[ptr + 1] <= x:
        ptr += 1
    return hull_k[ptr] * x + hull_b[ptr], ptr


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    a = data[1:1 + n]

    S = [0.0] * (n + 1)
    for i in range(1, n + 1):
        S[i] = S[i - 1] + a[i - 1]

    slopes_P = [-float(i) for i in range(n, -1, -1)]
    inter_P = [S[i] for i in range(n, -1, -1)]
    kP, bP, startP = build_upper_inc(slopes_P, inter_P)

    slopes_Q = [float(i) for i in range(n + 1)]
    inter_Q = [-S[i] for i in range(n + 1)]
    kQ, bQ, startQ = build_upper_inc(slopes_Q, inter_Q)

    xs = set(startP[1:])
    xs.update(startQ[1:])
    xs = sorted(xs)

    best = INF
    ptrP = ptrQ = 0

    for x in xs:
        up, ptrP = eval_hull(kP, bP, startP, x, ptrP)
        uq, ptrQ = eval_hull(kQ, bQ, startQ, x, ptrQ)
        val = up + uq
        if val < best:
            best = val

    print(f"{best:.6f}")

if __name__ == "__main__":
    main()
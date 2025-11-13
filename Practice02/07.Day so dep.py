from sys import stdin, stdout

if __name__ == "__main__":
    data = stdin.buffer.read().split()
    it = iter(data)
    for _ in range(int(next(it))):
        n = int(next(it))
        a = list(map(int, [next(it) for _ in range(n)]))
        cnt = 0
        for i in range(n - 1):
            mn = min(a[i], a[i + 1])
            mx = max(a[i], a[i + 1])
            while mn * 2 < mx:
                mn *= 2
                cnt += 1
        stdout.write(f"{cnt}\n")
        

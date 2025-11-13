def check(s):
    if s[-1] == '2' : 
        return False
    for ch in ['2', '3', '5', '7']:
        if ch not in s:
            return False
    return True

if __name__ == "__main__":
    n = int(input())
    digits = ['2', '3', '5', '7']
    results = []
    from itertools import product
    for tup in product(digits, repeat=n):
        s = ''.join(tup)
        if check(s):
            results.append(s)
    results.sort(key=lambda x: int(x))
    for res in results:
        print(res)


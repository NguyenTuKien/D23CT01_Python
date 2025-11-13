import math
from collections import deque

nto = "2357"
def check(s):
    if len(s) < 4:
        return False
    for i in nto:
        if i not in s:
            return False
    if s[len(s) - 1] == '2':
        return False
    return True

def gen(n):
    dq = deque(["2", "3", "5", "7"])
    while len(dq) != 0 and len(dq[0]) <= n:
        tmp = dq.popleft()
        if check(tmp):
            print(tmp)
        dq.append(tmp + "2")
        dq.append(tmp + "3")
        dq.append(tmp + "5")
        dq.append(tmp + "7")
    dq.clear()

if __name__ == "__main__":
    n = int(input())
    gen(n)
def check(cur):
    s = set(cur)
    if 'A' not in s or 'B' not in s or 'C' not in s:
        return False
    cntA = cur.count('A')
    cntB = cur.count('B')
    cntC = cur.count('C')
    if cntA > cntB or cntB > cntC : 
        return False
    return True

def gen(cur, length):
    if len(cur) == length:
        if(check(cur)):
            print(cur)
        return
    gen(cur + 'A', length)
    gen(cur + 'B', length)
    gen(cur + 'C', length)

if __name__ == "__main__":
    for i in range(3, int(input()) + 1):
        gen("", i)





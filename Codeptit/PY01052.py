def check(val):
    if int(val) < 2: return False
    for i in range(2, int(val ** 0.5) + 1):
        if val % i == 0:
            return False
    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        num = input()
        sum = 0
        for c in num:
            sum += int(c)
        if(check(sum)): 
            print("YES")
        else : 
            print("NO")
        
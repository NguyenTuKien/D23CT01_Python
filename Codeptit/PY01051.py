def check(num):
    if len(num) <= 1 : return False
    for i in range(len(num) // 2):
        if(num[i] != num[len(num) - i - 1]):
            return False
    return True
if __name__ == "__main__":
    for _ in range(int(input())):
        num = input()
        sum = 0
        for c in num:
            sum += int(c)
        if(check(str(sum))):
            print("YES")
        else : print("NO")
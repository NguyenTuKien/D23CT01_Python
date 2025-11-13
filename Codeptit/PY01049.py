import math

if __name__ == "__main__":
    prime = [True] * 505
    for i in range(2, int(math.sqrt(505))):
        if prime[i] :
            for j in range (i * i, 505, i):
                prime[j] = False
    for _ in range(int(input())):
        s = input()
        cnt = 0
        for c in s :
            if c == '2' or c == '3' or c == '5' or c == '7':
                cnt += 1
        if cnt > len(s) - cnt and prime[len(s)]:
            print("YES")
        else : 
            print("NO")

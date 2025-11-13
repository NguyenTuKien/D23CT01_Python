def backtrack(cur, max_len, marked=set()):
    if len(cur) == max_len:
        print(cur, end=' ')
        return
    for i in range(max_len, 0, -1):
        if i not in marked:
            marked.add(i)
            backtrack(cur + str(i), max_len, marked)
            marked.remove(i)

def count(max_len):
    count = max_len
    for i in range(2, max_len):
        count *= i
    return count


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        print(count(n))        
        backtrack("", n)
        print()
def HanoiTown(turn, src, des, tmp):
    if turn == 1:
        print(f"{src} -> {des}")
        return
    HanoiTown(turn - 1, src, tmp, des)
    print(f"{src} -> {des}")
    HanoiTown(turn - 1, tmp, des, src)

if __name__ == "__main__":
    n = int(input())
    HanoiTown(n, 'A', 'C', 'B')

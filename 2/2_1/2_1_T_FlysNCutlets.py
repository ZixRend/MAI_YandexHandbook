def solution(n: int, m: int, k1: int, k2: int):
    for i in range(1, n):
        if (n - i) * k1 + i * k2 == n * m:
            print(n - i, i)
            break


def main():
    n, m, k1, k2 = (int(input()) for _ in range(4))
    solution(n, m, k1, k2)


if __name__ == '__main__':
    main()

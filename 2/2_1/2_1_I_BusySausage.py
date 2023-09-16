def solution(n: int, m: int):
    print(m * n // 2)


def main():
    n, m = (int(input()) for _ in range(2))
    solution(n, m)


if __name__ == '__main__':
    main()

def solution(a: int, b: int, c: int):
    print('{:.2f}'.format(abs(b - a) / c))


def main():
    a, b, c = (int(input()) for _ in range(3))
    solution(a, b, c)


if __name__ == '__main__':
    main()

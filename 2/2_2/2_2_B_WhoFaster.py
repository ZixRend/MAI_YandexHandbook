def solution(v1: int, v2: int):
    print('Петя' if v1 > v2 else 'Вася')


def main():
    v1, v2 = (int(input()) for _ in range(2))
    solution(v1, v2)


if __name__ == '__main__':
    main()

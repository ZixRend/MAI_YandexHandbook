def solution(s: int, e: int):
    print(' '.join(map(str, range(s, e + 1))))


def main():
    s, e = (int(input()) for _ in range(2))
    solution(s, e)


if __name__ == '__main__':
    main()

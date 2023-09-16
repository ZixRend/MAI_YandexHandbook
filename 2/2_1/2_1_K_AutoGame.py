def solution(sub: str):
    print(''.join(sub[i] for i in (1, 0, 3, 2)))


def main():
    sub = input()
    solution(sub)


if __name__ == '__main__':
    main()

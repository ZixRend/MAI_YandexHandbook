def solution(num: str):
    num = list(map(int, list(num)))
    print(''.join(map(str, sorted([num[0] + num[1], num[1] + num[2]], reverse=True))))


def main():
    num = input()
    solution(num)


if __name__ == '__main__':
    main()

def solution(num: str):
    num = sorted(map(int, list(num)))
    print('YES' if num[0] + num[2] == num[1] * 2 else 'NO')


def main():
    num = input()
    solution(num)


if __name__ == '__main__':
    main()

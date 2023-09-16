def solution(num: str):
    print('YES' if num == num[::-1] else 'NO')


def main():
    num = input()
    solution(num)


if __name__ == '__main__':
    main()

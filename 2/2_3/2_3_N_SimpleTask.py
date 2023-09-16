def solution(num: int):
    print('YES' if not any(not num % i for i in range(2, int(num ** 0.5) + 1)) and num != 1 else 'NO')


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

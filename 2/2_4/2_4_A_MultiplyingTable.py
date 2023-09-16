def solution(num: int):
    for i in range(1, num + 1):
        print(' '.join(f'{i * j}' for j in range(1, num + 1)))


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

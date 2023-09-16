def solution(height: int, length: int):
    k = len(str(height * length))
    for i in range(1, height * length + 1):
        if i % length:
            print(f'{" " * (k - len(str(i)))}{i}', end=' ')
        else:
            print(f'{" " * (k - len(str(i)))}{i}')


def main():
    height, length = (int(input()) for _ in range(2))
    solution(height, length)


if __name__ == '__main__':
    main()

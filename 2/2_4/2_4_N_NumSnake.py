def solution(height: int, length: int):
    k = len(str(height * length))
    temp = []
    for i in range(1, height * length + 1):
        if i % length:
            temp.append(f'{" " * (k - len(str(i)))}{i}')
        else:
            temp.append(f'{" " * (k - len(str(i)))}{i}')
            if (i // length) % 2:
                print(' '.join(temp))
            else:
                print(' '.join(temp[::-1]))
            temp = []


def main():
    height, length = (int(input()) for _ in range(2))
    solution(height, length)


if __name__ == '__main__':
    main()

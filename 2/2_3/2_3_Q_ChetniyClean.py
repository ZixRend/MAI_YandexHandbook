def solution(num: str):
    print(''.join(str(i) for i in map(int, num) if i % 2))


def main():
    num = input()
    solution(num)


if __name__ == '__main__':
    main()

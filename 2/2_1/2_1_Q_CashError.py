def solution(num: int, bi_num: str):
    print(num + int(bi_num, 2))


def main():
    num = int(input())
    bi_num = input()
    solution(num, bi_num)


if __name__ == '__main__':
    main()

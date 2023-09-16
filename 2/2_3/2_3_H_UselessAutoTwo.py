def solution(sub: str, count_a: int):
    print('\n'.join([sub] * count_a))


def main():
    sub = input()
    count_a = int(input())
    solution(sub, count_a)


if __name__ == '__main__':
    main()

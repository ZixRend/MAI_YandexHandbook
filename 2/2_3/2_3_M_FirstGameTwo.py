def solution(names: list):
    print(sorted(names)[0])


def main():
    count_a = int(input())
    names = [input() for _ in range(count_a)]
    solution(names)


if __name__ == '__main__':
    main()

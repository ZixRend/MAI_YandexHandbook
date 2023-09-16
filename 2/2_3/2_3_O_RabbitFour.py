def solution(forest: list):
    print(sum('зайка' in i for i in forest))


def main():
    count_a = int(input())
    forest = [input() for _ in range(count_a)]
    solution(forest)


if __name__ == '__main__':
    main()

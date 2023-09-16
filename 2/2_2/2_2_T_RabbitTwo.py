def solution(forest: list):
    for i in forest:
        if 'зайка' in i:
            print(i, len(i))
            break


def main():
    forest = sorted(input() for _ in range(3))
    solution(forest)


if __name__ == '__main__':
    main()

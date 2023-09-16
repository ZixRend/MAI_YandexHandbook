def solution(count_a: int):
    print(count_a)


def main():
    count_a = 0
    while (sub := input()) != 'Приехали!':
        count_a += 'зайка' in sub
    solution(count_a)


if __name__ == '__main__':
    main()

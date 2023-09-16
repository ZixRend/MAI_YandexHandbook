def solution():
    ...


def main():
    s, e = 1, 1001
    while (x := input(f'{(s + e) // 2}\n')) != 'Угадал!':
        if x == 'Меньше':
            e = (s + e) // 2
        elif x == 'Больше':
            s = (s + e) // 2
    solution()


if __name__ == '__main__':
    main()

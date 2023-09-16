def solution(n: int, m: int):
    petya, vasya = 7, 6
    petya, vasya = petya - 3, vasya + 3
    petya += 2
    vasya += 5 - 2
    petya += n
    vasya += m
    print('Петя' if petya > vasya else 'Вася')


def main():
    n, m = (int(input()) for _ in range(2))
    solution(n, m)


if __name__ == '__main__':
    main()

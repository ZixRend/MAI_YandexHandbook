from calendar import isleap


def solution(year: int):
    print('YES' if isleap(year) else 'NO')


def main():
    year = int(input())
    solution(year)


if __name__ == '__main__':
    main()

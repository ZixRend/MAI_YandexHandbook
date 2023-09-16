def solution(x: int, y: int):
    print(y, x, sep='\n')


def main():
    x, y = 0, 0
    while (name := input()) != 'СТОП':
        if name == 'СЕВЕР':
            y += int(input())
        elif name == 'ВОСТОК':
            x += int(input())
        elif name == 'ЮГ':
            y -= int(input())
        else:
            x -= int(input())
    solution(x, y)


if __name__ == '__main__':
    main()

def solution(red: int, blue: int):
    print(red + blue + 1)


def main():
    red, green, blue = (int(input()) for _ in range(3))
    solution(red, blue)


if __name__ == '__main__':
    main()

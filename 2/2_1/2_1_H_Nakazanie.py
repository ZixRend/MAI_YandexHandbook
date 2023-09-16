def solution(num: int, string: str):
    sub = [f'Я больше никогда не буду писать "{string}"!'] * num
    print('\n'.join(sub))


def main():
    num = int(input())
    string = input()
    solution(num, string)


if __name__ == '__main__':
    main()

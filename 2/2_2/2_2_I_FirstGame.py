def solution(names: list):
    print(sorted(names)[0])


def main():
    names = [input() for _ in range(3)]
    solution(names)


if __name__ == '__main__':
    main()

def solution(sub: str):
    new_sub = [sub] * 3
    print('\n'.join(new_sub))


def main():
    sub = input()
    solution(sub)


if __name__ == '__main__':
    main()

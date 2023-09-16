def solution(speeds: list):
    top = {i: j for i, j in zip(speeds, ('Петя', 'Вася', 'Толя'))}
    top = dict(sorted(top.items(), reverse=True))
    sub = list(top.values())
    print(f'{"": ^8}{sub[0]: ^8}{"": ^8}', f'{sub[1]: ^8}{"": ^8}{"": ^8}', f'{"": ^8}{"": ^8}{sub[2]: ^8}', sep='\n')
    print(f'{"II": ^8}{"I": ^8}{"III": ^8}')


def main():
    speeds = [int(input()) for _ in range(3)]
    solution(speeds)


if __name__ == '__main__':
    main()

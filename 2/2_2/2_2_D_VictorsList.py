def solution(speeds: list):
    top = {i: j for i, j in zip(speeds, ('Петя', 'Вася', 'Толя'))}
    top = dict(sorted(top.items(), reverse=True))
    sub = '\n'.join(f'{num + 1}. {name}' for num, name in enumerate(top.values()))
    print(sub)


def main():
    speeds = [int(input()) for _ in range(3)]
    solution(speeds)


if __name__ == '__main__':
    main()

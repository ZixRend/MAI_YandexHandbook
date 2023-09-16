def solution(n: int, m: int, t: int):
    minutes = m + t
    hours = n + minutes // 60
    print(f'{hours % 24:0>2}:{minutes % 60:0>2}')


def main():
    n, m, t = (int(input()) for _ in range(3))
    solution(n, m, t)


if __name__ == '__main__':
    main()

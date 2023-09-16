def solution(num: int):
    for i in range(1, num + 1):
        print(*[f'{j} * {i} = {i * j}' for j in range(1, num + 1)], sep='\n')


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

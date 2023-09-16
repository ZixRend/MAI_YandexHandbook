def solution(num: int):
    for i in range(3, 3 + num):
        for j in range(i, 0, -1):
            print(f'До старта {j} секунд(ы)')
        print(f'Старт {i - 2}!!!')


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

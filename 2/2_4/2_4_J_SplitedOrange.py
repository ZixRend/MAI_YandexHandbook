def solution(num: int):
    print('А Б В')
    for x in range(num):
        for y in range(num):
            for z in range(num):
                if sum([x, y, z]) == num - 3:
                    print(x + 1, y + 1, z + 1)


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

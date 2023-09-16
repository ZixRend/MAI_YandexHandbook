def solution(num: int):
    bad_nums = set(sum(range(i)) for i in range(num + 1))
    temp = []
    for i in range(1, num + 1):
        if i in bad_nums:
            temp.append(str(i))
            print(' '.join(temp))
            temp = []
        else:
            temp.append(str(i))
    if len(temp):
        print(' '.join(temp))


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

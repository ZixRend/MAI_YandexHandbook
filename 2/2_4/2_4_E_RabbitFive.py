def solution(check: int):
    print(check)


def main():
    check = 0
    count_a = int(input())
    for _ in range(count_a):
        flag = False
        while (sub := input()) != 'ВСЁ':
            if sub == 'зайка':
                flag = True
        check += flag
    solution(check)


if __name__ == '__main__':
    main()

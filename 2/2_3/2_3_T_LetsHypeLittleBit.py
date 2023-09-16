def solution(result: int):
    print(result)


def main():
    result, hn1 = -1, 0
    for i in range(int(input())):
        b = int(input())
        h, r, m = b % 256, (b // 256) % 256, (b // 256 ** 2) % 256
        temp = (37 * (m + r + hn1)) % 256
        if temp != h or h > 99:
            result = i
            break
        hn1 = h
    solution(result)


if __name__ == '__main__':
    main()

def solution(num: int):
    nums = []
    for i in range(2, num + 1):
        while not num % i:
            nums.append(str(i))
            num //= i
    print(' * '.join(nums))


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

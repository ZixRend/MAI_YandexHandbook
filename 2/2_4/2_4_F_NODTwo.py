from math import gcd


def solution(nums: list):
    print(gcd(*nums))


def main():
    count_a = int(input())
    nums = [int(input()) for _ in range(count_a)]
    solution(nums)


if __name__ == '__main__':
    main()

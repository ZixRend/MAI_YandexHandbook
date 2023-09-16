from math import lcm


def solution(nums: list):
    print(lcm(*nums))


def main():
    nums = [int(input()) for _ in range(2)]
    solution(nums)


if __name__ == '__main__':
    main()

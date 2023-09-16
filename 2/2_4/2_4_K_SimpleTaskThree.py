def solution(nums: list):
    print(len(list(filter(lambda num: not any(not num % i for i in range(2, int(num ** 0.5) + 1)) and num > 1, nums))))


def main():
    num = int(input())
    nums = [int(input()) for _ in range(num)]
    solution(nums)


if __name__ == '__main__':
    main()

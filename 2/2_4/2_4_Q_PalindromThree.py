def solution(nums: list):
    print(sum(i == i[::-1] for i in nums))


def main():
    num = int(input())
    nums = [input() for _ in range(num)]
    solution(nums)


if __name__ == '__main__':
    main()

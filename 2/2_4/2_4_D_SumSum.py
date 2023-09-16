def solution(nums: list):
    print(sum(sum(map(int, i)) for i in nums))


def main():
    count_a = int(input())
    nums = [input() for _ in range(count_a)]
    solution(nums)


if __name__ == '__main__':
    main()

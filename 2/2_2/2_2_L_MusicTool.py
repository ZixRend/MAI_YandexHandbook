def solution(nums: list):
    print('YES' if nums[0] + nums[1] > nums[2] else 'NO')


def main():
    nums = sorted(int(input()) for _ in range(3))
    solution(nums)


if __name__ == '__main__':
    main()

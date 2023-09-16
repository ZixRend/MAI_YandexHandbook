def solution(nums: list):
    if nums[0] ** 2 + nums[1] ** 2 < nums[2] ** 2:
        print('велика')
    elif nums[0] ** 2 + nums[1] ** 2 == nums[2] ** 2:
        print('100%')
    else:
        print('крайне мала')


def main():
    nums = sorted(int(input()) for _ in range(3))
    solution(nums)


if __name__ == '__main__':
    main()

def solution(nums: list):
    print(f'{nums[-1]}{sum(nums[1:][:-1]) % 10}{nums[0]}')


def main():
    nums = sorted(int(j) for i in (input() for _ in range(2)) for j in i)
    solution(nums)


if __name__ == '__main__':
    main()

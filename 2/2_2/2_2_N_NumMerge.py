from itertools import permutations


def solution(nums: str):
    new_nums = [''.join(i) for i in permutations(nums, 2)]
    new_nums = [int(i) for i in new_nums if len(str(int(i))) == 2]
    print(min(new_nums), max(new_nums))


def main():
    nums = input().removeprefix('-')
    solution(nums)


if __name__ == '__main__':
    main()

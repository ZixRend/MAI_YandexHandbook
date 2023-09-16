def solution(nums: list):
    w = ['Петя', 'Вася', 'Толя']
    status = nums.index(max(nums))
    print(w[status])


def main():
    nums = [int(input()) for _ in range(3)]
    solution(nums)


if __name__ == '__main__':
    main()

def solution(nums: list):
    print(round(sum(nums), 1))


def main():
    nums = []
    while (num := input()) != '0':
        nums.append(float(num) if float(num) < 500 else float(num) * 0.9)
    solution(nums)


if __name__ == '__main__':
    main()

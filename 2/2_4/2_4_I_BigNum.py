def solution(nums: list):
    print(''.join(nums))


def main():
    num = int(input())
    nums = [str(max(map(int, input()))) for _ in range(num)]
    solution(nums)


if __name__ == '__main__':
    main()

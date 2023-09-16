def solution(height: int, length: int):
    nums = [['0'] * height for _ in range(height)]
    for i in range(height):
        for j in range(height):
            if not length % 2:
                nums[i][j] = str((i + 1) * (j + 1)).center(length)
            else:
                nums[i][j] = str((i + 1) * (j + 1))[::-1].center(length)[::-1]
    nums = ['|'.join(i) for i in nums]
    print(*nums, sep=f'\n{(length * height + height - 1) * "-"}\n')


def main():
    height, length = (int(input()) for _ in range(2))
    solution(height, length)


if __name__ == '__main__':
    main()

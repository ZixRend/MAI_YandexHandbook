def solution(height: int, length: int):
    nums = []
    for i in range(1, height + 1):
        for j in range(length):
            nums.append(i + j * height)
    k = len(str(height * length))
    nums = [f'{" " * (k - len(str(i)))}{i}' for i in nums]
    temp = []
    for i in range(height * length):
        if i % length or not i:
            temp.append(nums[i])
        else:
            print(' '.join(temp))
            temp = [nums[i]]
    if len(temp):
        print(' '.join(temp))


def main():
    height, length = (int(input()) for _ in range(2))
    solution(height, length)


if __name__ == '__main__':
    main()

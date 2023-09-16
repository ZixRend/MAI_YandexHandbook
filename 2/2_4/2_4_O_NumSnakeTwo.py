def solution(height: int, length: int):
    k = len(str(height * length))
    nums = [[] for _ in range(height)]
    temp = []
    for i in range(1, height * length + 1):
        if i % height:
            temp.append(f'{" " * (k - len(str(i)))}{i}')
        else:
            temp.append(f'{" " * (k - len(str(i)))}{i}')
            for j in range(height):
                if (i // height) % 2:
                    nums[j].append(temp[j])
                else:
                    nums[j].append(temp[-j - 1])
            temp = []
    print(*[' '.join(i) for i in nums], sep='\n')


def main():
    height, length = (int(input()) for _ in range(2))
    solution(height, length)


if __name__ == '__main__':
    main()

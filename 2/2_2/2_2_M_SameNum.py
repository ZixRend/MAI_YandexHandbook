def solution(num1: str, num2: str, num3: str):
    for x, y, z in zip(num1, num2, num3):
        if x == y == z:
            print(x)


def main():
    num1, num2, num3 = (input() for _ in range(3))
    solution(num1, num2, num3)


if __name__ == '__main__':
    main()

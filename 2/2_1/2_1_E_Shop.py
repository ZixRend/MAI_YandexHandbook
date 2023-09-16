def solution(money: int, price: int, weight: int):
    print(money - price * weight)


def main():
    price, weight, money = (int(input()) for _ in range(3))
    solution(money, price, weight)


if __name__ == '__main__':
    main()

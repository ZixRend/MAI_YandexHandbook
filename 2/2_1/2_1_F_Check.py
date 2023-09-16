def solution(name: str, money: int, price: int, weight: int):
    output = str('Чек\n{} - {}кг - {}руб/кг\nИтого: {}руб\nВнесено: {}руб'
                 '\nСдача: {}руб'.format(name, weight, price, weight * price,
                                         money, money - weight * price))
    print(output)


def main():
    name = input()
    price, weight, money = (int(input()) for _ in range(3))
    solution(name, money, price, weight)


if __name__ == '__main__':
    main()

def solution(item: str, price: int, weight: int, money: int):
    real_price = f'{weight}кг * {price}руб/кг'
    sub = str(f'{"Чек":=^35}\nТовар:{item: >29}\n'
              f'Цена:{real_price: >30}\n'
              f'Итого:{price * weight: >26}руб\n'
              f'Внесено:{money: >24}руб\n'
              f'Сдача:{money - price * weight: >26}руб\n'
              f'{"=" * 35}')
    print(sub)


def main():
    item = input()
    price, weight, money = (int(input()) for _ in range(3))
    solution(item, price, weight, money)


if __name__ == '__main__':
    main()

def solution(x: float, y: float):
    if (x ** 2 + y ** 2) ** 0.5 > 10:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    elif any([x >= 0 and y >= 0 and (x ** 2 + y ** 2) ** 0.5 <= 5,
              -4 <= x < 0 <= y <= 5,
              -7 <= x < -4 and 5 >= y >= 0 and 5 * x - 3 * y > -35,
              0.25 * x ** 2 + 0.5 * x - 8.75 <= y <= 0]):
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')


def main():
    x, y = (float(input()) for _ in range(2))
    solution(x, y)


if __name__ == '__main__':
    main()

def solution(a: float, b: float, c: float):
    if not any((a, b, c)):
        print('Infinite solutions')
    elif not a and not b and c or b ** 2 - 4 * a * c < 0:
        print('No solution')
    elif not b ** 2 - 4 * a * c:
        print(f'{-b / (2 * a):.2f}')
    elif not a:
        print(f'{-c / b:.2f}')
    else:
        roots = sorted([(-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a), (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)])
        print(f'{roots[0]:.2f} {roots[1]:.2f}')


def main():
    a, b, c = (float(input()) for _ in range(3))
    solution(a, b, c)


if __name__ == '__main__':
    main()

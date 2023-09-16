def solution(name: str, num: str):
    sub = str(f'Группа №{num[0]}.\n{num[-1]}. {name}.\nШкафчик: {num}.'
              f'\nКроватка: {num[1]}.')
    print(sub)


def main():
    name, num = (input() for _ in range(2))
    solution(name, num)


if __name__ == '__main__':
    main()

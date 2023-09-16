def solution(feeling: str):
    w = {'хорошо': 'Я за вас рада!', 'плохо': 'Всё наладится!'}
    if feeling in w.keys():
        print(w[feeling])


def main():
    name = input('Как Вас зовут?\n')
    feeling = input(f'Здравствуйте, {name}!\nКак дела?\n')
    solution(feeling)


if __name__ == '__main__':
    main()

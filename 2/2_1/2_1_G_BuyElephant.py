def solution(count_a: int):
    new_sub = ['Купи слона!'] * count_a
    print('\n'.join(new_sub))


def main():
    count_a = int(input())
    solution(count_a)


if __name__ == '__main__':
    main()

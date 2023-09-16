def solution(sub1: str, sub2: str):
    new_sub1 = list(map(int, f'{sub1:0>3}'))
    new_sub2 = list(map(int, f'{sub2:0>3}'))
    print('{}{}{}'.format((new_sub1[0] + new_sub2[0]) % 10,
                          (new_sub1[1] + new_sub2[1]) % 10,
                          (new_sub1[2] + new_sub2[2]) % 10))


def main():
    sub1, sub2 = (input() for _ in range(2))
    solution(sub1, sub2)


if __name__ == '__main__':
    main()

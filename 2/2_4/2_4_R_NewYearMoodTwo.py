def solution(num: int, lengths: list):
    helper = 1
    for i in range(1, num + 1):
        if i - 1 in (sum(range(v)) for v in range(i + 2)):
            print(f"{' ' * ((max(lengths) - lengths[helper]) // 2)}{i}", end=' ' if i != 1 else '\n')
            helper += 1
        else:
            print(i, end='\n' if i in (sum(range(v)) for v in range(i + 2)) else ' ')


def main():
    x, lengths = '', [0]
    for i in range(1, (num := int(input())) + 1):
        x += f'{i} '
        if i in (sum(range(j)) for j in range(i + 2)):
            lengths.append(len(x) - 1)
            x = ''
    lengths.append(len(x) - 1)
    solution(num, lengths)


if __name__ == '__main__':
    main()

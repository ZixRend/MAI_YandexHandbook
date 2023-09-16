def solution(num: int):
    def change_base(n: int, base: int):
        res = ''
        while n:
            temp = n % base
            n //= base
            res += str(temp) if temp < 10 else chr(temp + 55)
        return sum(map(int, res[::-1]))
    voc = {i: float('-inf') for i in range(2, 11)}
    for i in range(2, 11):
        voc[i] = change_base(num, i)
    print([x for x, y in voc.items() if y == max(voc.values())][0])


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

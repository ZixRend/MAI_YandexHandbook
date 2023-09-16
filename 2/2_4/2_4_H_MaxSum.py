def solution(voc: dict):
    voc = sorted(voc.items())
    print(voc[-1][1])


def main():
    num = int(input())
    voc = {}
    for _ in range(num):
        value = input()
        key = sum(map(int, input()))
        voc[key] = value
    solution(voc)


if __name__ == '__main__':
    main()

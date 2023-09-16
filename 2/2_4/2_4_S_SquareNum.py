def solution(num: int):
    k = len(str(num // 2 + num % 2))
    all_builds = []
    builder = [1] * num
    for i in range(1, num + 1):
        if i <= num // 2 + num % 2:
            all_builds.append(builder)
            print(' '.join([j[::-1].center(k)[::-1] for j in map(str, builder)]))
            builder = list(builder[0:i] + [j + 1 for j in builder[i:num - i]] + builder[num - i:num + 1])
        else:
            if num % 2:
                print(' '.join(j[::-1].center(k)[::-1] for j in map(str, all_builds[-2])))
            else:
                print(' '.join(j[::-1].center(k)[::-1] for j in map(str, all_builds[-1])))
            all_builds.pop(-1)


def main():
    num = int(input())
    solution(num)


if __name__ == '__main__':
    main()

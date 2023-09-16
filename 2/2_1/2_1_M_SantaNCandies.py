def solution(child_num: int, candies: int):
    print(candies // child_num, candies % child_num, sep='\n')


def main():
    child_num = int(input())
    candies = int(input())
    solution(child_num, candies)


if __name__ == '__main__':
    main()

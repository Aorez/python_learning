# from distance import distance
#
# print(distance(1, 2))

def hourglass(n: int, step: int):
    str = ""
    for i in range(0, step - 1):
        str += " "
    for i in range(0, n - step):
        str += "**"
    str += "*"
    if step == n:
        print(str)
    else:
        print(str)
        hourglass(n, step + 1)
        print(str)


def main():
    try:
        while True:
            n = eval(input())
            hourglass(n, 1)
    except EOFError:
        pass


if __name__ == '__main__':
    main()
# 14x+8y=2n

def main():
    try:
        while True:
            n = eval(input())
            for cock in range(0, 2 * n // 14 + 1):
                hen = 2 * n - 14 * cock
                if hen % 8 == 0:
                    hen = hen // 8
                    chick = n - cock - hen
                    print(cock, hen, chick)
    except EOFError:
        pass

if __name__ == '__main__':
    main()
a, b = input().split()
a, b = int(a), int(b)
charArray = ("+", "-", "*", "/")
for i in range(4):
    c = int(eval("a" + charArray[i] + "b"))
    print("{} {} {} = {}".format(a, charArray[i], b, c))
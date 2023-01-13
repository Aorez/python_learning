narcissus = [[], [], [], [], [], []]

for i in range(100, 100000):
    digit = len(str(i))
    numberSquence = list(map(int, str(i)))
    sum = 0
    for j in numberSquence:
        sum += j ** digit
    if sum == i:
        narcissus[digit].append(i)

for i in range(3, 6):
    print(i, "位水仙花数：")
    print(narcissus[i])
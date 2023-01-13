lis = input().split()
dic = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for it in lis:
    if int(it) in range(0, 60):
        dic['F'] += 1
    elif int(it) in range(60, 70):
        dic['D'] += 1
    elif int(it) in range(70, 80):
        dic['C'] += 1
    elif int(it) in range(80, 90):
        dic['B'] += 1
    else:
        dic['A'] += 1
for it in dic.items():
    print(it[0] + ': ' + str(it[1]))

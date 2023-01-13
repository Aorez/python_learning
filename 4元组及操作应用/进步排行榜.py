t = int(input())
for T in range(t):
    n = int(input())
    lis = []
    for N in range(n):
        lis.append(list(map(str, input().split())))
    lis = sorted(lis, key=lambda x: (-int(x[1]), -int(x[2]), x[0]))
    lis[0].append(1)
    pre = 1
    for i in range(1, n):
        if lis[i][1] == lis[i - 1][1] and lis[i][2] == lis[i - 1][2]:
            lis[i].append(pre)
        else:
            lis[i].append(i + 1)
            pre = i + 1
    for i in range(n):
        print('{} {} {} {}'.format(lis[i][3], lis[i][0], lis[i][1], lis[i][2]))

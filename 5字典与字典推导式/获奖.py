t = int(input())
for T in range(t):
    n, ms = input().split()
    n = int(n)
    rank = round(n * 0.6)
    lis = []
    for N in range(n):
        s, m, g = input().split()
        m = int(m)
        g = int(g)
        lis.append([s, m, g])
    lis = sorted(lis, key=lambda x: (-x[1], -x[2]))
    # print(lis)
    for ind in range(n):
        # print(ind)
        if ind + 1 > rank:
            print("NO")
            break
        if lis[ind][0] == ms:
            print("YES")
            break
# 1
# 3 team001
# team001 2 27
# team002 2 28
# team003 0 7

lis = eval(input())
lis2 = []
[lis2.append(it) for it in lis if it not in lis2]
for it in lis2[:-1]:
    print(it, end=' ')
print(lis2[-1])

lis = [125, 86, 147, 91, 177, 94, 150, 102, 175, 130]
ans = []
now = 125
while True:
    ans.append(now)
    lis = sorted(lis)
    nowi = lis.index(now)
    pre = lis[nowi - 1] if nowi - 1 >= 0 else -1
    nex = lis[nowi + 1] if nowi + 1 < len(lis) else -1
    lis.remove(now)
    if pre == -1 and nex == -1:
        break
    elif pre == -1:
        now = nex
    elif nex == -1:
        now = pre
    else:
        now = pre if now-pre < now-nex else nex
print(ans)
coun = 0
for i in range(len(ans)-1):
    coun += abs(ans[i]-ans[i+1])
print(coun)

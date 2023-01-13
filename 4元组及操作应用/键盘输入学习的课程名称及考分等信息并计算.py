lis = []
total = 0
while True:
    lis2 = input().split()
    if not lis2:
        break
    lis.append(lis2)
    total += int(lis2[1])
lis = sorted(lis, key=lambda x: -int(x[1]))
# 最高分课程是语文95, 最低分课程是物理84, 平均分是88.40
print("最高分课程是{}{}, 最低分课程是{}{}, 平均分是{:.2f}".format(lis[0][0], lis[0][1], lis[len(lis) - 1][0], lis[len(lis) - 1][1], total / len(lis)))

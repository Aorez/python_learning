age = 0
dic = {'男': 0, '女': 0}
count = 0

while True:
    lis = input().split()
    if not lis:
        break
    dic[lis[1]] += 1
    age += int(lis[2])
    count += 1

print("平均年龄是{:.2f} 男性人数是{}".format(age / count, dic['男']))

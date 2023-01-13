lis1 = input().split(',')
lis2 = input().split(',')
x = eval(input())
# lis1 = '5 10, 8 5, -1 1, 10 0 '.split(',')
lis1 = [[int(i) for i in it.split()] for it in lis1]
lis2 = [[int(i) for i in it.split()] for it in lis2]
dic1 = {ke: val for val, ke in lis1}
dic2 = {ke: val for val, ke in lis2}
dic3 = {}
for ke, va in dic1.items():
    dic3[ke] = va + dic2.get(ke, 0)
for ke, va in dic2.items():
    if dic1.get(ke, 0) == 0:
        dic3[ke] = va
print(dic3[x])

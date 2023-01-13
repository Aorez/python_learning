dic1 = eval(input())
# print(dic1)
dic2 = eval(input())
# print(dic2)
dic3 = {}
for ke, va in dic1.items():
    dic3[ke] = va + dic2.get(ke, 0)
for ke, va in dic2.items():
    if ke not in dic1:
        dic3[ke] = va
lis = sorted(dic3.items(), key=lambda x: x[0] if isinstance(x[0], int) else ord(x[0]))
stri = str(dict(lis)).replace(" ", "")
stri = stri.replace("'", "\"")
print(stri)

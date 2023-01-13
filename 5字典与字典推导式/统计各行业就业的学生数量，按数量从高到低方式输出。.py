lis = input().split()
dic = {ke: lis.count(ke) for ke in lis}
# print(dic)
# 交通 金融 计算机 交通 计算机 计算机
dic = dict(sorted(dic.items(), key=lambda x: -x[1]))
stri = str(dic).replace("'", "")
stri = stri.replace(" ", "")
stri = stri.replace(",", "\n")
print(stri[1:-1])

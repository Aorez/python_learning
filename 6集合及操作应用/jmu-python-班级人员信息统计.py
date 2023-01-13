classa = set(input())
classb = set(input().split())
classab = classa | classb
acm = set(input().split())
eng = set(input().split())
trans = input()
# print(classa)
# print(classb)
# print(classab)
# print(acm)
# print(eng)
# print(trans)
print("Total: {}".format(len(classb) + len(classa)))
lis = sorted(classab - acm - eng)
print("Not in race: {}, num: {}".format(lis, len(lis)))
lis = sorted(acm | eng)
print("All racers: {}, num: {}".format(lis, len(lis)))
lis = sorted(acm & eng)
print("ACM + English: {}, num: {}".format(lis, len(lis)))
lis = sorted(acm - eng)
print("Only ACM: {}".format(lis))
lis = sorted(eng - acm)
print("Only English: {}".format(lis))
lis = sorted((acm - eng) | (eng - acm))
print("ACM Or English: {}".format(lis))
if trans in classb:
    print(sorted(classb - {trans}))
if trans in classa:
    print(sorted(classa - {trans}))
# abcdefghijab
# 1   2 3 4 5 6 7 8 9  10
# 1 2 3 a b c
# 1 5 10 a d e f
# 1


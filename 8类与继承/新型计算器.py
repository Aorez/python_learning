from functools import singledispatch


class VecCal:
    def __init__(self, x=0, y=0, z=0):
        self.X = x
        self.Y = y
        self.Z = z

    def __add__(self, n):
        return VecCal(self.X + n.X, self.Y + n.Y, self.Z + n.Z)

    def __sub__(self, n):
        return VecCal(self.X - n.X, self.Y - n.Y, self.Z - n.Z)

    # @singledispatch
    # def __mul__(self, n):
    #     return self.X * n.X + self.Y * n.Y + self.Z * n.Z
    #
    # @__mul__.register(int)
    # def _(self, n):
    #     return VecCal(self.X * n, self.Y * n, self.Z * n)

    def __mul__(self, n: int):
        return VecCal(self.X * n, self.Y * n, self.Z * n)

    def __truediv__(self, n: int):
        if n == 0:
            return VecCal()
        return VecCal(self.X // n, self.Y // n, self.Z // n)

    def __str__(self):
        return str((self.X, self.Y, self.Z))


# @singledispatch
# def f(x):
#     print("other{}".format(x))
#
#
# @f.register(int)
# def _(x):
#     print("int{}".format(x))
#
#
# f(1)
# f("a")

# a = VecCal(1, 1, 1)
# b = VecCal(2, 2, 2)
# print(a * 3)
# print(a / 1)
lis = list(map(int, input().split(",")))
a = VecCal(lis[0], lis[1], lis[2])
lis = list(map(int, input().split(",")))
b = VecCal(lis[0], lis[1], lis[2])
c = int(input())
# print(a)
# print(b)
# print(c)
stri = "{} {} {} = {}"
print(stri.format(a, '+', b, a + b))
print(stri.format(a, '-', b, a - b))
print(stri.format(a, '*', c, a * c))
print(stri.format(a, '/', c, a / c))

# 1,2,3
# 4,5,6
# 3

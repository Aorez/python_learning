import types


class InvestmentMaster:
    nowadaysYear = 2022

    def __init__(self):
        self.name = "匿名"
        self.sex = "男"
        self.age = 1
        self.wealth = 0

    def init(self, name: str, sex: str, age: int, initialWealth: int):
        self.name = name
        self.sex = sex
        self.age = age
        self.wealth = initialWealth

    def investment(self, investmentWay: str):
        if investmentWay == "股票投资":
            self.wealth += 2000
        elif investmentWay == "基金投资":
            self.wealth += 1500
        elif investmentWay == "债券投资":
            self.wealth += 1000

    def printer(self):
        print(self.nowadaysYear, self.name, self.sex, self.age, self.wealth)


person1 = InvestmentMaster()
person1.init("liuxiaoxiao", "女", 18, 1000)
person1.printer()
person1.investment("股票投资")
person1.printer()

person1.height = 170
print(person1.height)

person2 = InvestmentMaster()


# print(person2.height)


def setHeight(self, height: int):
    self.height = height


person2.setHeight = types.MethodType(setHeight, person2)
person2.setHeight(169)
print(person2.height)

person1.nowadaysYear = 2018
person1.printer()
person2.printer()
InvestmentMaster.nowadaysYear = 2017
person1.printer()
person2.printer()


class A:
    def sayHello(self):
        print("Ahello")


class B(A):
    def sayHello(self):
        print("Bhello")


class C(A):
    def sayHello(self):
        print("Chello")


class D(A):
    def sayHello(self):
        print("Dhello")


# 广度优先
class E(C, B, D):
    pass
    # def sayHello(self):
    #     print("Dhello")


e = E()
e.sayHello()


class User:
    def __init__(self, username="未设置", password="123456"):
        self.__password = password
        self.__username = username

    @property
    # setter前面要有property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if username.isdigit():
            return False
        else:
            self.__username = username
            return True


user1 = User()
# print(user1.__password)
# 不用括号
user1name = user1.username
print(user1name)
user1.username = "123"
print(user1.username)
user1.username = "abc"
print(user1.username)

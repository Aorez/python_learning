from math import sqrt


class Rect:
    def __init__(self, l, h, z):
        self.l = l
        self.h = h
        self.z = z

    def length(self):
        return 2 * (self.l + self.h)

    def area(self):
        return self.l * self.h


class Cubic(Rect):
    def __init__(self, l, h, z):
        super(Cubic, self).__init__(l, h, z)

    def area(self):
        return 2 * (self.l * self.h + self.l * self.z + self.h * self.z)

    def volume(self):
        return super(Cubic, self).area() * self.z


class Pyramid(Rect):
    def __init__(self, l, h, z):
        super(Pyramid, self).__init__(l, h, z)

    def area(self):
        return self.l * self.h + sqrt((self.h ** 2) / 4 + self.z ** 2) * self.l + \
               sqrt((self.l ** 2) / 4 + self.z ** 2) * self.h

    def volume(self):
        return super(Pyramid, self).area() * self.z / 3


while True:
    try:
        lis = list(map(float, input().split()))
        if not lis:
            continue
        # print(lis)
        # if not lis:
        #     break
        if lis[0] <= 0 or lis[1] <= 0 or lis[2] <= 0:
            print("0.00 0.00 0.00 0.00")
            continue
        cubic1 = Cubic(lis[0], lis[1], lis[2])
        pyra1 = Pyramid(lis[0], lis[1], lis[2])
        print("{:.2f} {:.2f} {:.2f} {:.2f}".format(cubic1.area(), cubic1.volume(), pyra1.area(), pyra1.volume()))
    except:
        break

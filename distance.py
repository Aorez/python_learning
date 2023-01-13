import math

def distance(*coordinate):
    count = len(coordinate)
    if count % 2 == 1:
        print("参数有误")
        return
    count //= 2
    xDistance = abs(coordinate[count] - coordinate[0])
    finalDistance = 0
    for i in range(0, count):
        finalDistance += (coordinate[i] - coordinate[i + count]) ** 2
    finalDistance = math.sqrt(finalDistance)
    return xDistance, finalDistance
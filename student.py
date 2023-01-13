import random

numberString = "学号:2018"
studentInformation = {"学号:2018" + str(i).zfill(2): {"语文": random.randint(50, 150), "数学": random.randint(50, 150), "英语": random.randint(50, 150)} for i in range(1, 41)}
for i in studentInformation:
    studentInformation[i]["总分"] = sum(studentInformation[i].values())
sortedInfo = sorted(studentInformation.items(), key = lambda x: x[1]["总分"], reverse = True)
for i in sortedInfo:
    print(i)
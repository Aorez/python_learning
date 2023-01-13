speed = eval(input())
limit = eval(input())
if speed <= limit:
    print("未超速", end = "")
else:
    rate = (speed - limit) / limit
    if rate <= 0.1:
        print("超速警告", end = "")
    elif rate <= 0.2:
        print("罚款100元", end = "")
    elif rate <= 0.5:
        print("罚款500元", end = "")
    elif rate <= 1:
        print("罚款1000元", end = "")
    else:
        print("罚款2000元", end = "")
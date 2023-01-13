def bonus(profit: float):
    if profit <= 100000:
        return profit * 0.1
    elif profit <= 200000:
        return (profit - 100000) * 0.075 + bonus(100000)
    elif profit <= 400000:
        return (profit - 200000) * 0.05 + bonus(200000)
    elif profit <= 600000:
        return (profit - 400000) * 0.03 + bonus(400000)
    elif profit <= 1000000:
        return (profit - 600000) * 0.015 + bonus(600000)
    else:
        return (profit - 1000000) * 0.01 + bonus(1000000)

p = eval(input())
print("%.2f"%bonus(p), end = "")
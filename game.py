import random

role = {"player": [5, 2, 3, 4], "monster": [10, 1, 2]}

while role["player"][0] > 0 and role["monster"][0] > 0:
    n = random.randint(1, 2)
    攻击者 = "monster"
    被攻击者 = "player"
    if n == 1:
        攻击者 = "player"
        被攻击者 = "monster"
    choice = random.choice(role[攻击者][1: len(role[攻击者])])
    role[被攻击者][0] -= choice
if role["player"][0] > 0:
    print("玩家胜利")
    print("剩余血量为：")
    print(role["player"][0])
else:
    print("怪物胜利")
    print("剩余血量为：")
    print(role["monster"][0])
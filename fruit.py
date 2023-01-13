import random

store = {"apple": 1, "banana": 2, "watermelon": 3}
stock = set(["pear", "cherry", "apple", "orange"])
n = len(stock) // 2
for i in range(n):
    choice = random.choice(list(stock))
    addNum = random.randint(1, 10)
    if store.get(choice) is None:
        store[choice] = addNum
    else:
        store[choice] += addNum
sortedStore = sorted(store.items(), key = lambda x: x[1])
print("商店水果：")
print(sortedStore)
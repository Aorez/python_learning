se = set(map(int, input().split()))
ans = 0
for num in se:
    ans += num
print("{:.3f}".format(ans / len(se)))

from collections import defaultdict

n = int(input())
fMap = defaultdict(int)
for i in range(n):
    array = input().split()
    for j in array[1:]:
        fMap[int(j)] += 1
answerArray = sorted(fMap.items(), key = lambda x:x[1], reverse = True)
max = answerArray[0][1]
maxmax = answerArray[0][0]
for i in answerArray[1:]:
    if i[1] == max:
        if i[0] > maxmax:
            maxmax = i[0]
    else:
        break
print(maxmax, max)
import csv
import json

with open('score2.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    list2 = list(reader)

for i in range(1, len(list2)):
    list2[i] = dict(zip(list2[0], list2[i]))

with open('score2.json', 'w', encoding='utf-8') as f:
    json.dump(list2[1:], f, sort_keys=True, ensure_ascii=False, indent=4)

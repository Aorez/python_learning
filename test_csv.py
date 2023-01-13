import csv

data = "00 80 80 81 81 14 8C 00 01 85 82 24 8C 10\n\
10 88 14 C8 20 34 FC\n\
20 80 81 CC\n\
80 02 03 00 00\n"
print(data.replace("\n", ""))

with open('.\\test_csv.txt', 'w', encoding='utf-8') as f:
    f.write(data)

lis = []
with open('test_csv.txt', 'r') as f:
    for line in f:
        lis.append(line.replace("\n", "").split(" "))
print(lis)

with open('test_csv.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    writer.writerows(lis)

with open("test_csv.csv", "r") as f:
    reader = csv.reader(f)
    print(list(reader))

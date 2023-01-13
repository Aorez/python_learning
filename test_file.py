with open("test.txt", 'w', encoding='utf-8', errors='ignore') as f, open("test2.txt", 'wb') as f2:
    f.write("")
    f2.write(b"ab")

with open("test.txt", 'a', encoding='utf-8') as f:
    f.write("1232312adsfalafds")

print(len("1232312adsfalafd正"))

with open('test.txt', 'r', encoding='utf-8') as f:
    print(f.read(1))
    p = f.tell()
    print(p)
    print(f.readline())
    p2 = f.tell()
    print(p2)
    f.seek(1, 0)
    print(f.readline())
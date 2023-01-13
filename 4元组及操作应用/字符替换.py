lis = [[chr(x), chr(155 - x)] for x in range(65, 91)]
stri = input()
stri2 = ""
for it in stri:
    if it.isupper():
        for it2 in lis:
            if ord(it) == ord(it2[0]):
                stri2 += it2[1]
                break
    else:
        stri2 += it
print(stri2)

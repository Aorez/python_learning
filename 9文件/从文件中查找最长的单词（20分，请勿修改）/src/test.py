"""
data.txt中保存有n个单词，每个单词一行。
请编写一个程序从文件中将单词读出，找到最长的单词，
然后将其保存到result.txt中。程序须保存test.py中

输出格式：

用以下格式输出最长的字符串到**result.txt**中:
The longest word is: zhang
如果有多个单词，则每个单词用**英文逗号**间隔(结尾无**逗号**)：
The longest words are: zhang,xiang

样例1: 测试失败(同sample)
样例2: 测试失败(有两个同样长的单词，且行两侧有空格)
样例3: 测试失败(只有一个最长的单词)
样例4: 测试失败(单词有重复)
样例5: 测试失败(单词内有空格)

"""

with open("data.txt", 'r', encoding='utf-8') as fil:
    txt = fil.readlines()
longest = []
maxlen = 0
for word in txt:
    word = word.strip()
    if len(word) > maxlen:
        longest = [word]
        maxlen = len(word)
    elif len(word) == maxlen:
        longest.append(word)
with open("result.txt", 'w', encoding='utf-8') as fil:
    if len(longest) == 1:
        fil.write("The longest word is: {}".format(longest[0]))
    else:
        longest = ','.join(longest)
        fil.write("The longest words are: {}".format(longest))

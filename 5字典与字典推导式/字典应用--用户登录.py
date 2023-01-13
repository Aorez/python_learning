dic = {'admin': '123456', 'administrator': '12345678', 'root': 'password'}


def check(user_name, password):
    global dic
    if user_name not in dic:  # 判断是否输入错误账号
        return 0
    if dic[user_name] == password:
        return 1
    return 0


user_name2 = input()
password2 = input()
if check(user_name2, password2):
    print('登录成功')
else:
    print('登录失败')
    for i in range(2):
        user_name2 = input()
        password2 = input()
        if check(user_name2, password2):
            print('登录成功')
            break
        else:
            print('登录失败')

# 验证用户名与密码


count = 0
while count < 3:
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == 'admin' and password == '123456':
        print('身份验证成功！')
        break
    else:
        print('身份验证失败！')
        count += 1
    if count == 3:
        print('身份验证失败次数过多，程序退出！')


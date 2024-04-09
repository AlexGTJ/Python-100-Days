import random

answer = random.randint(1, 100)
counter = 0
while True:
    try:
        number = int(input('请输入: '))
        counter += 1
    except ValueError:
        print('输入有误，请输入一个整数')
        continue

    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break
print('你总共猜了%d次' % counter)
if counter > 7:
    print('你的智商余额明显不足')

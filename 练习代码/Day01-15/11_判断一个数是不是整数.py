# 判断一个数是否是整数
# 1. 输入一个数字

num = float(input('请输入一个数字：'))
# 2. 判断这个数字是否是整数
if num % 1 == 0:
    print('%d是整数' % num)
else:
    print('%.2f不是整数' % num)
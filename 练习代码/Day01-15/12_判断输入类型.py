# 判断input函数输入的值的类型
# 1. 输入一个值
# 2. 判断这个值的类型
# 3. 输出这个值的类型
#
value = input('请输入一个值：')

if value.isdigit():
    print('%s是整数' % value)
elif value.isalpha():
    print('%s是字符串' % value)
else:
    print('%s是其他类型' % value)

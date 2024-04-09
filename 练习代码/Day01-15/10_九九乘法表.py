# Filename: 10_九九乘法表.py
for col in range(1, 10):
    for row in range(1, col + 1):
        print('%d*%d=%d' % (col, row, col * row), end='\t')
    print()

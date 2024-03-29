while True:
    try:
        value = float(input('请输入长度：'))
        unit = input('请输入单位(in/cm/英寸/厘米)：')
        if unit == 'in' or unit == '英寸':
            print('%.2f英寸 = %.2f厘米' % (value, value * 2.54))
            continue
        elif unit == 'cm' or unit == '厘米':
            print('%.2f厘米 = %.2f英寸' % (value, value / 2.54))
            continue
        else:
            print('输入的不是有效单位！')
            result = input('是否需要退出程序？(y/n)：') 
            if result == 'y':
                break
            else:
                continue
    except ValueError:
        print("输入的不是一个有效的数字。")
        result = input('是否需要退出程序？(y/n)：') 
        if result == 'y':
            break
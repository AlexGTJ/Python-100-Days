# 给出半径，计算园的面积和周长
# 使用tutle库绘制图形
import math
import turtle

# 创建一个turtle绘图窗口，宽高分别为800，600
turtle.setup(800, 600)

# 在窗口中设置一个用户输入的文本框
r = turtle.numinput("输入半径", "请输入圆的半径：")
s = round(math.pi * r * r,2)
l = round(2 * math.pi * r,2)

# 画圆
turtle.pensize(4)
turtle.pencolor('red')
turtle.circle(r)


# 把圆的面积和周长画在画布的display位置，保存2位小数
turtle.penup()
turtle.goto(0, -200)
turtle.pendown()
turtle.write("圆的面积是：" + str(s), align="center", font=("Arial", 24, "normal"))
turtle.penup()
turtle.goto(0, -230)
turtle.pendown()
turtle.write("圆的周长是：" + str(l), align="center", font=("Arial", 24, "normal"))
turtle.done()
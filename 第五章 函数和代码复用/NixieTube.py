# 七段数码管绘制
import turtle


def drawLine(draw):
    turtle.Pen.down() if draw else turtle.Pen.up()
    turtle.Pen.fd(40)
    turtle.Pen.right(90)


# 绘制一个数码管
def drawDigit(digit):
    drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
    turtle.Pen.left(90)
    drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.Pen.left(180)
    turtle.Pen.up() # 为绘制后续数字确定位置
    turtle.Pen.fd(20)


# 绘制多个数码管
def drawDate(date):
    for i in date:
        drawDigit(eval(i))



# turtle.Pen.up()
# turtle.Pen.fd(-300)
drawDate('20210728')
turtle.done()






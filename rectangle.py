Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
tao = turtle.Pen()
tao.shape('turtle')
def Rectangle():
    for i in range(4):
        tao.fd(300)
        tao.left(90)

        
Rectangle()
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

    
Go(-200,-100)
def Circle():
    for i in range(10):
        tao.circle(80)
        tao.left(36)

        
Circle()

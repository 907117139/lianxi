import turtle
import time

def drawsnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.pencolor("black")
        turtle.circle(rad,angle)
        turtle.circle(-rad, angle)
    turtle.pencolor("red")
    turtle.circle(rad, angle/2)
    turtle.pencolor("purple")
    turtle.fd(rad)
    turtle.pencolor("yellow")
    turtle.circle(neckrad+1,180)
    turtle.pencolor("green")
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.seth(-40)
    drawsnake(40,80,5,pythonsize/2)

main()
time.sleep(3)
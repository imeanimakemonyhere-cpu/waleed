#python: skip-file
import math
import time 
from turtle import *

def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)
speed(100)
bgcolor("black")
color("white")
hideturtle()
while True:
    for scale in range(20, 30):
        clear()
        begin_fill()
        for i in range(360):
            x = hearta(math.radians(i)) * scale
            y = heartb(math.radians(i)) * scale
            goto(x, y)
        end_fill()
        time.sleep(0.05)

    for scale in range(30, 20, -1):
        clear()
        begin_fill()
        for i in range(360):
            x = hearta(math.radins(i)) * scale
            y = heartb(math.radins(i)) * scale 
            goto(x, y)
        end_fill()
        time.sleep(0.05)
    done()


    





    
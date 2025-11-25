#draw a holow heart from the inside like mine.  print("pretty corny)

import math 
from turtle import *

def heart(k):
    return 15 * math.sin(k)**3

def heart1(k):
    return (13 * math.cos(k)
            - 5 * math.cos(2 * k)
            - 2 * math.cos(3 * k)
            - math.cos(4 * k))

speed(0)
bgcolor("black")
hideturtle()
color("pink")  

for i in range(0, 450):
    goto(heart(i) * 20, heart1(i) * 20)

done()




    











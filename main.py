#Import these turtle sleep
#turtle = is the line which is named turtle
#time = to wait for few secs and then program the next thing
import turtle
import time

navi_turtle = turtle.Turtle()


# define(def) used to make bunches of code it one short define to use it any time.ex: def square()
#this code is to make a 8 with two squares.
#the right could be changed into left both work the same.
def square():
  navi_turtle.forward(100)
  navi_turtle.right(90)
  navi_turtle.forward(100)
  navi_turtle.right(90)
  navi_turtle.forward(100)
  navi_turtle.right(90)
  navi_turtle.forward(100)
  navi_turtle.forward(100)
  navi_turtle.right(90)
  navi_turtle.forward(200)
  navi_turtle.right(90)
  navi_turtle.forward(100)
  navi_turtle.right(90)
  navi_turtle.forward(100)
  navi_turtle.right(90)
  navi_turtle.forward(100)
  navi_turtle.right(180)
  navi_turtle.forward(200)
  navi_turtle.left(90)
  navi_turtle.forward(100)
  navi_turtle.left(90)
  navi_turtle.forward(200)
  time.sleep(0.5)
#this is a example how the define works

elephant_weight = 6000
whale_weight = 150000

#if elephant_weight < whale_weight:
 #square()
#else:
 #navi_turtle.forward(90)

for count in range(6):
    square()
navi_turtle.right(90)
navi_turtle.forward(100)
navi_turtle.right(90)
navi_turtle.forward(200)
navi_turtle.right(90)
navi_turtle.forward(500)
navi_turtle.right(90)
navi_turtle.forward(500)
navi_turtle.right(90)
navi_turtle.forward(500)
navi_turtle.right(90)
navi_turtle.forward(300)


import turtle
from turtle import Turtle, Screen
import  random
t = Turtle()
turtle.colormode(255)
def random_color():
  r= random.randint(0,255)
  g= random.randint(0,255)
  b= random.randint(0,255)
  color = (r,g,b)
  return color
t.shape("turtle")
t.speed("fastest")
def draw_spirograph(size_of_gap):
  for _ in range(int( 360/size_of_gap)):
    t.color(random_color())
    t.circle(100)
    t.setheading(t.heading()+size_of_gap)

draw_spirograph(5)

































# directions =[0,90,180,270]

# for _ in range(5):
#   t.color(random_color())
#   # t.forward(30)
#   # t.setheading(random.choice(directions))
#   t.home()
#   t.position()
#   t.circle(50)























# def draw_shape(num_sides):
#    angle = 360/num_sides
#    for _ in range(num_sides):
#
#       t.forward(100)
#       t.right(angle)
#
#
# for shape in range(3,11):
#
#    t.color(random.choice(colors))
#    draw_shape(shape)



















screen = Screen()

screen.exitonclick()
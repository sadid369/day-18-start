from turtle import Turtle, Screen
import  random
t = Turtle()
t.shape("turtle")
colors = ["dim gray", "chartreuse", "peru", "orange red", "magenta", "dark violet"]
def draw_shape(num_sides):
   angle = 360/num_sides
   for _ in range(num_sides):
      t.forward(100)
      t.right(angle)

for shape in range(3,11):
   t.color(random.choice(colors))
   draw_shape(shape)



















screen = Screen()

screen.exitonclick()
# Import modules
from turtle import *

# Start program
color('red')
begin_fill()
pensize(5)
setposition(0,0)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
penup()
setposition(0,200)
pendown()

# Write text
write("I love you", font=("sans-serif",18,"normal"), align="center")
hideturtle()
done()

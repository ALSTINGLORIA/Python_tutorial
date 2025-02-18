import turtle

t = turtle.Turtle()

length = int(input("Enter the length of the star's sides: "))

fill_color = input("Enter the fill color for the star: ")

screen = turtle.Screen()

t.fillcolor(fill_color)
t.pencolor(fill_color)
t.begin_fill()


for i in range(5):
    t.forward(length) 
    t.right(144)  

t.end_fill()

turtle.done()

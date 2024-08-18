import turtle

wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")

ank = turtle.Turtle()
ank.color('white')

hello = turtle.Turtle()
hello.color('red')
hello.fillcolor('red')
hello.begin_fill()


hello.left(140) 
hello.forward(180)  
hello.circle(-90, 220) 

world = turtle.Turtle()
world.color('red')
world.fillcolor('red')
world.begin_fill()

world.left(40)
world.forward(180)
world.circle(90,220)

hello.hideturtle()
world.hideturtle()

hello.end_fill()
world.end_fill()

ank.goto(3,0)
ank.write("Tiyasha",font=("Arial",20, "bold"))

wn.mainloop()
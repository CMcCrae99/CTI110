import turtle          
win = turtle.Screen()  
t = turtle.Turtle()

for i in [0,1,2]:
# add some display options
    t.pensize(9)            # increase pensize (takes integer)
    t.pencolor("green")     # set pencolor (takes string)
    t.shape("triangle")

#commands from here to the last line can be replaced
# triangle, sides are 360 / 3 = 120 degrees

    t.forward(100)          
    t.left(120)            
    t.forward(100)
    t.left(120)

for i in [0,1]:
# Commands for square
    t.pensize(7)
    t.pencolor("brown")
    t.shape("square")

    t.forward(50)          # Move forward by 50 units
    t.left(90)             # Turn by 90 degrees
    t.forward(50)
    t.left(90)
# end commands
win.mainloop()             # Wait for user to close window

import turtle 
t = turtle.Pen() 
for x in range(50):
    t.color("red")
    t.forward(x*10) 
    t.left(90)
    t.color("blue")
    t.forward(x*10) 
    t.left(90)
   

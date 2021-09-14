import turtle as t

def move_w():
    t.setheading(90)
    t.forward(50)
    t.stamp()
    
def move_a():
    t.setheading(180)
    t.forward(50)
    t.stamp()

def move_s():
    t.setheading(-90)
    t.forward(50)
    t.stamp()

def move_d():
    t.setheading(0)
    t.forward(50)
    t.stamp()

def restart():
    t.reset()

t.shape('turtle')

t.onkey(restart,'Escape')
t.onkey(move_w,'w')
t.onkey(move_a,'a')
t.onkey(move_s,'s')
t.onkey(move_d,'d')
t.listen()

input()

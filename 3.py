import random
from turtle import *
colormode(255)
bgcolor(0,153,255)

jazmine = Turtle()
jade = Turtle()
meower = Turtle()

jazmine.shape('turtle')
jazmine.color('yellow')
jazmine.speed(10)

jade.shape('turtle')
jade.color('green')

meower.shape('turtle')
meower.color('purple')

def draw_star(t, x, y, points, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()

    turn = 180 - (360 / points)
    
    t.color(line, fill)

    t.begin_fill()
    for i in range (points):
        t.forward (200)
        t.left (turn)
    t.end_fill()

def draw_grass(t, x, y, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(line, fill)
    t.begin_fill()
    t.forward(1300)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(1310)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(10)

    t.end_fill()
    
def draw_house(t, x, y, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(line, fill)
    t.begin_fill()
    t.forward(350)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(350)
    t.right(90)
    t.forward(350)
    t.right(50)
    t.forward(225)
    t.right(79)
    t.forward(231)
        
    t.end_fill()
        
def draw_window(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.left(39)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.penup()
    t.right(90)
    t.forward(170)
    t.pendown()
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(80)

def draw_door(t, x, y, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(line, fill)
    t.begin_fill()
    t.right(90)
    t.forward(110)
    t.left(90)
    t.forward(130)
    t.left(90)
    t.forward(70)
    t.left(90)
    t.forward(128)
    t.end_fill()
    
def draw_bottom(t, x, y, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(line, fill)
    t.begin_fill()
    t.forward(80)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(100)
    t.end_fill()

def draw_tree(t, x, y, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(line, fill)
    t.begin_fill()
    t.forward(120)
    t.left(120)
    t.forward(220)
    t.left(120)
    t.forward(220)
    t.left(120)
    t.forward(100)
    t.end_fill()
    
def draw_mailbox(t, x, y, line, fill):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(line, fill)
    t.begin_fill()
    t.left(90)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(100)
    t.right(90)
    t.forward(80)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(110)
    t.end_fill()
    
    

def draw_stick(t, x, y, line, fill):
    t.right(180)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pendown()
    t.color(line, fill)
    t.begin_fill()
    t.forward(50)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(20)
    t.end_fill()
    

draw_star(jade, 0, 390, 36, 'orange', 'yellow')
draw_star(jazmine, -250, 390, 18,  'orange', 'yellow')
draw_star(meower, -500, 390, 20, 'orange', 'yellow')
draw_star(jade, 250, 390, 12, 'orange', 'yellow')
draw_grass(meower, -627, -350, 'green', 'green')
draw_house(jade, 100, 0, 'black', 'white')
draw_window(jade, 150, -48)
draw_door(jade, 200, -350, 'black', 'brown')
draw_tree(jazmine, -220, -250, 'black', 'green')
draw_bottom(meower, -250, -350, 'black', 'brown')
draw_mailbox(meower, -400, -150, 'black', 'pink')
draw_stick(jade, -460, -100, 'black', 'red')

# and now run around randomly
all_turtles = (jazmine, jade, meower)

MAX_DISTANCE_FROM_CENTER = 500

while True:
    for t in all_turtles:
        rand_dir = random.randint(-20, 20)
        rand_dist = random.randint(5, 10)
        
        t.right(rand_dir)
        t.forward(rand_dist)

        pos = t.position()
        x = pos[0]
        y = pos[1]

        if (x < -MAX_DISTANCE_FROM_CENTER or x > MAX_DISTANCE_FROM_CENTER) or (y < -MAX_DISTANCE_FROM_CENTER or y > MAX_DISTANCE_FROM_CENTER):
            direction = t.towards(0, 0)
            t.setheading(direction)

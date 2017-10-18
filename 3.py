import random
from turtle import *

jazmine = Turtle()
jade = Turtle()
meower = Turtle()

jazmine.shape('turtle')
jazmine.color('green')
jazmine.speed(10)

jade.shape('turtle')
jade.color('blue')

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



draw_star(jade, 0, 0, 36, 'orange', 'blue')
draw_star(jazmine, -300, -300, 18,  'pink', 'purple')
draw_star(meower, -300, 200, 20, 'blue', 'yellow')
draw_star(jade, 250, 100, 12, 'blue', 'pink')

meower.forward(50)
jade.back(50)

for i in range (10):
    jazmine.left(60)
    jazmine.forward(80)
    jazmine.right(80)
    jazmine.forward(40)
    
    jade.right(60)
    jade.left(80)
    jade.back(100)
    
    meower.forward(60)
    meower.left(90)
    meower.right(45)
    



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

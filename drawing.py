from turtle import*

def draw_star(x, y, points, line, fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)
    
    color(line, fill)

    begin_fill()
    for i in range (points):
        forward (200)
        left (turn)
    end_fill()


speed(10)

draw_star(0, 0, 36, 'orange', 'blue')
draw_star(-300, -300, 18,  'pink', 'purple')
draw_star(-300, 200, 50, 'blue', 'yellow')
draw_star(250, 100, 12, 'blue', 'yellow')

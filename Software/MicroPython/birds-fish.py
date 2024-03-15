import turtle


turtle.speed(200)

def rondine(posizione, rotazione, dimensione):
    turtle.penup()
    turtle.home()
    turtle.forward(posizione)
    turtle.pendown()
    turtle.right(rotazione)
    turtle.circle(dimensione, 40)
    turtle.right(90)
    turtle.circle(dimensione, 40)

rondine( 0, 200, 50 )
rondine( 100, 220, 70 )
rondine( 250, 160, 90 )

turtle.done()
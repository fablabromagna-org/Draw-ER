#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import turtle

primoSegmento = 12
segmento = 10
segmento_indietro = 3*primoSegmento

turtle.pendown()

for x in range(8):
 
    for y in range(3):
        turtle.forward(primoSegmento)
        turtle.right(45)
        turtle.forward(segmento)
        turtle.penup()
        turtle.backward(segmento)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(segmento)
        turtle.penup()
        turtle.backward(segmento)
        turtle.pendown()
        turtle.right(45)

    turtle.backward(segmento_indietro)
    turtle.right(45)

turtle.done()

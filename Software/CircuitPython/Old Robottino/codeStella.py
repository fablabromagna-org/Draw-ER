import board
import time
import FLRturtle as FLRTurtle

primoSegmento = 12
segmento = 10
segmento_indietro = 3*primoSegmento

FLRTurtle.pendown()

for x in range(8):
  
    for y in range(3):
        FLRTurtle.forward(primoSegmento)
        FLRTurtle.right(45)
        FLRTurtle.forward(segmento)
        FLRTurtle.penup()
        FLRTurtle.backward(segmento)
        FLRTurtle.pendown()
        FLRTurtle.left(90)
        FLRTurtle.forward(segmento)
        FLRTurtle.penup()
        FLRTurtle.backward(segmento)
        FLRTurtle.pendown()
        FLRTurtle.right(45)

    FLRTurtle.backward(segmento_indietro)
    FLRTurtle.right(45)

FLRTurtle.penup()
FLRTurtle.done()
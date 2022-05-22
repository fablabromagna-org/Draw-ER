#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "disegna un fiocco di neve come Anna di code.org" )

primoSegmento = 12
segmento = 10
segmento_indietro = 3*primoSegmento

pendown()

for x in range(8):
  
    for y in range(3):
        forward(primoSegmento)
        right(45)
        forward(segmento)
        penup()
        backward(segmento)
        pendown()
        left(90)
        forward(segmento)
        penup()
        backward(segmento)
        pendown()
        right(45)

    backward(segmento_indietro)
    right(45)

# spegne i motori e risparmia energia
penup()
done()

#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "disegna un fiocco di neve tipo 1 MakersBox" )

# Attenzione.
# Sul robottino questi due metodi non danno errore ma non possono funzionare
pensize(5)
pencolor('skyblue')

arms = 5
length = 50
angle = 60

pendown()
for arm in range(arms):
    forward(length)
    right(angle)
    forward(length)
    left(angle)
    backward(length)
    right(angle)
    backward(length)
    right(360 / arms - angle)

penup()
setheading(90)  # North
forward(100)

# spegne i motori e risparmia energia
penup()
done()

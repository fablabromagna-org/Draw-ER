#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "disegna un fiocco di neve tipo 2 MakersBox" )

# Attenzione.
# Sul robottino questi due metodi non danno errore ma non possono funzionare
pensize(5)
pencolor('skyblue')

number_of_arms = 6  # Change this variable to add arms
length = 30         # Change is variable to change snowflake size

def draw(length):
    # this is a simple flunction to draw forward, lift pen, move backward
    pendown()
    forward(length)
    penup()
    backward(length)

for arm in range(number_of_arms):
  pendown()
  forward(length * 1.5)
  right(45)
  draw(length)
  left(90)
  pendown()
  draw(length)
  right(45)
  backward(length * 1.5)
  left(360 / number_of_arms)

# spegne i motori e risparmia energia
penup()
done()  

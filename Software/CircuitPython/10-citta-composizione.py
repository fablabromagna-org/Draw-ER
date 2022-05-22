#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#

import time
from turtle import *

print( "disegna una citta (micromondo)" )

def facciata():
    pendown()
    for x in range(4):
        forward(100)
        right(90)
    penup()

def tetto():
    pendown()
    for x in range(3):
        forward(100)
        left(120)
    penup()

def casa():
    facciata()
    tetto()
    
def paese():    
    casa()
    #penup()

    right(15)
    forward(130)
    left(15)

    #pendown()
    casa()
    #penup()

    left(5)
    forward(120)
    right(5)
    #pendown()

def citta():
    paese()
    paese()
    paese()
   
# Si posiziona più indietro e disegna una città    
penup()
backward(400)
citta()

# spegne i motori e risparmia energia
done()



#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "disegna un quadrato definendo una funzione (o metodo)" )

def quadrato():
    pendown()
    for x in range(4):
        forward(100)
        right(90)
    penup()

# chiama il metodo "quadrato"
quadrato()

# spegne i motori e risparmia energia
done()

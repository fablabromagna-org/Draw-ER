#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "disegna una stella usando un ciclo for" )


#stella proposta nelle slide
#for x in range(40):
#    forward(100)
#    right(140)
#    forward(100)
#    left(90)

# stella doppia appuntita
#for x in range(9):
#    forward(100)
#    right(170)
#    forward(100)
#    left(90)

# lama da taglio
for x in range(9):
    forward(100)
    right(140)
    forward(20)
    left(100)

done()

#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "Disegna poligoni parametrici" )

#parametro in ingresso
lati = 8

#calcoli preliminari
angolo = 360/lati
segmento = 80

#disegna poligono
for x in range(lati):
    forward(segmento)
    right(angolo)

# spegne i motori e risparmia energia
done()

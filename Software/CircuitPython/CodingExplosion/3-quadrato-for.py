#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "disegna un quadrato usando un ciclo for" )

numero_lati = 4
lunghezza = 100

# avanti di 100 (4 volte)
for lato in range( numero_lati ):
    forward( lunghezza )
    right( 360/numero_lati )

# spegne i motori e risparmia energia
done()

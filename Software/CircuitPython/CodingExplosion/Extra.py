import time
from turtle import *

print( "disegna una linea" )

def quadrato():
    # avanti di 100 (4 volte)
    for x in range(4):
        forward( 100 )
        right( 90 )

def stella():
    punte = 4
    dimensione = 80
    quantoEAppuntita = 150

    angolo1 = quantoEAppuntita
    angolo2 = quantoEAppuntita - (360/punte)

    ## sposta la tartaruga di 100 passi (circa 10cm sul robot)
    for x in range( punte ):
        forward( dimensione )
        right( angolo1 )
        forward( dimensione )
        left( angolo2 )

quadrato()
stella()

print( "Finito!!" )

# spegne i motori e risparmia energia
penup()
done()

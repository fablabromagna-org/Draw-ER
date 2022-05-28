#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import turtle

print( "disegna un quadrato usando un ciclo for" )

lati = 150
lato = 3

# avanti di 100 (4 volte)
for lato in range( lati ):
    forward( lato )
    right( 360/lati )


# spegne i motori e risparmia energia
done()

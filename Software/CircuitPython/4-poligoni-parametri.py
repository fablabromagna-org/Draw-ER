#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import turtle
print( "Disegna poligoni parametrici" )

# parametri in ingresso
lati = 5
lato = 80

turtle.pendown()

# esegue “lati” volte le istruzioni
for x in range(lati):
    angolo = 360/lati
    turtle.forward(lato)
    turtle.right(angolo)

# domanda:
# Ci sono delle istruzioni che sprecano energia?
# Se eseguiamo 100 volte il corpo del for... 

# spegne i motori e risparmia energia
done()

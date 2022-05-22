# Importo la libreria
from turtle import *

print("Hello python!!")

# Parametri dell'utente
numero_dei_lati = 9
lunghezza_lato = 50

# calcoli automatici...
angoloDestro = 140
angoloSinistro = 100

# Disegno
for giro in range( numero_dei_lati ) :
    forward( lunghezza_lato )
    right( angoloDestro )
    forward( lunghezza_lato )
    left( angoloSinistro )

# Spengo il robottino
done()
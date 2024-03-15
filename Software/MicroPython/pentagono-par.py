import turtle

# dico come si chiama e cosa deve fare
def poligono(lati, lato):
  angolo = 360/lati
  for x in range(lati):
    turtle.forward(lato)
    turtle.right(angolo)

# lo fa
poligono(5, 100)

turtle.done()
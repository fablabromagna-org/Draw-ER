import turtle

# dico come si chiama e cosa deve fare
def poligono(lati, lato):
  angolo = 360/lati
  for x in range(lati):
    turtle.forward(lato)
    turtle.right(angolo)

turtle.speed(200)

# lo fa
for x in range(30):
    poligono(4, 100)
    turtle.right(360/30)

turtle.done()
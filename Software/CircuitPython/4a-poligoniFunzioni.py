import turtle as turtle

#disegna poligono
def poligono(lati, lato):
  angolo = 360/lati
  for x in range(lati):
    turtle.forward(lato)
    turtle.right(angolo)

poligono(5, 100)
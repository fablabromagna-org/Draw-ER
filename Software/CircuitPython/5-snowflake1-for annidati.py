#
# Coding Explosion!
# 10-11-2021
#
# Elisabetta Siboni e Maurizio Conti
# Servizio Marconi - USR-ER 2021
#
import time
from turtle import *

print( "disegna un fiocco di neve come Anna di code.org" )

for x in range(8):
  
  for y in range(3):
    forward(40)
    right(45)
    forward(30)
    backward(30)
    left(90)
    forward(30)
    backward(30)
    right(45)
  
  backward(120)
  right(45)

# spegne i motori e risparmia energia
done()

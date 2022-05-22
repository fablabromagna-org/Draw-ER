import board
import FLRturtle

print( "FabLab Turtle" )
FLRturtle.setDebug( True )

FLRturtle.pendown()

for x in range( 0, 4 ):
    FLRturtle.forward( 40 )   # muove in avanti
    FLRturtle.right( 90 )     # gira a destra

FLRturtle.done()          # Fine!

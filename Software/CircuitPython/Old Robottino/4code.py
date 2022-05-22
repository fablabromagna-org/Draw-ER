import board
import time
import FLRturtle

print( "FabLab Turtle" )
FLRturtle.setDebug( True )

FLRturtle.pendown()
#time.sleep(0.2)
#FLRturtle.circle(10)

for x in range(0,4):
    FLRturtle.forward( 40 )   # move turtle out of the way
    FLRturtle.penup()
    time.sleep(0.2)
    FLRturtle.forward( 5.5 )   # move turtle out of the way
    FLRturtle.right( 90 )     # move turtle right
    FLRturtle.backward( 6 )   # move turtle out of the way

    FLRturtle.pendown()
    time.sleep(0.2)

FLRturtle.done()          # Fine!

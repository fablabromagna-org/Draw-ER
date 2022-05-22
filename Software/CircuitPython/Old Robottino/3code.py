import board
import time
import FLRturtle

print( "FabLab Turtle" )
FLRturtle.setDebug( True )

FLRturtle.pendown()

FLRturtle.forward( 40 )   # muove in avanti

FLRturtle.penup()         # solleva la penna
time.sleep(0.2)           # aspetta poco

FLRturtle.forward( 5.5 )   # move turtle out of the way
FLRturtle.right( 90 )     # 
FLRturtle.backward( 6 )   # 
FLRturtle.pendown()
time.sleep(0.2)

FLRturtle.forward( 40 )   # muove in avanti

FLRturtle.penup()         # solleva la penna
time.sleep(0.2)           # aspetta poco

FLRturtle.forward( 5.5 )   # move turtle out of the way
FLRturtle.right( 90 )     # 
FLRturtle.backward( 6 )   # 
FLRturtle.pendown()
time.sleep(0.2)

FLRturtle.done()          # Fine!

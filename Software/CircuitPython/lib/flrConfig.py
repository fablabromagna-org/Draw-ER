import sys
if sys.platform == "RP2040":
    ## Per slow turtle (robottino)
    import board
    import time
    import FLRturtle as turtle
    turtle.setDebug( True )
    print( "FLR robot on", sys.platform )
else:
# Per fast Turtle (PC)
    import turtle

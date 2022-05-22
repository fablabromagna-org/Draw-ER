from machine import Pin
import time

Q8 = Pin(5, Pin.OUT)
Q7 = Pin(2, Pin.OUT)
Q6 = Pin(3, Pin.OUT)
Q5 = Pin(4, Pin.OUT)

Q4 = Pin(7, Pin.OUT)
Q3 = Pin(8, Pin.OUT)
Q2 = Pin(10, Pin.OUT)
Q1 = Pin(6, Pin.OUT)

LEDBlu = Q4

LEDS = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8]

for led in LEDS:
    led.value(1)
    time.sleep_ms(100)
    
for led in LEDS:
    led.value(0)
    time.sleep_ms(100)
    

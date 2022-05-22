import machine
import utime

led_onboard = machine.Pin(2, machine.Pin.OUT)
D0 = machine.Pin(16, machine.Pin.OUT)
D1 = machine.Pin(5, machine.Pin.OUT)
D2 = machine.Pin(4, machine.Pin.OUT)
D3 = machine.Pin(0, machine.Pin.OUT)

A1 = D0
A2 = D1
B1 = D2
B2 = D3

tempo = 1000

def active_low_step() :

    A1.value(0)
    A2.value(1)
    B1.value(1)
    B2.value(1)
    utime.sleep_us(tempo)

    #step2
    A1.value(0)
    A2.value(0)
    B1.value(1)
    B2.value(1)
    utime.sleep_us(tempo)

    A1.value(1)
    A2.value(0)
    B1.value(1)
    B2.value(1)
    utime.sleep_us(tempo)

    A1.value(1)
    A2.value(0)
    B1.value(0)
    B2.value(1)
    utime.sleep_us(tempo)

    A1.value(1)
    A2.value(1)
    B1.value(0)
    B2.value(1)
    utime.sleep_us(tempo)

    #step1
    A1.value(1)
    A2.value(1)
    B1.value(0)
    B2.value(0)
    utime.sleep_us(tempo)

    A1.value(1)
    A2.value(1)
    B1.value(1)
    B2.value(0)
    utime.sleep_us(tempo)

    A1.value(0)
    A2.value(1)
    B1.value(1)
    B2.value(0)
    utime.sleep_us(tempo)

def Lstep() :

    B2.value(1)
    utime.sleep_us(tempo)

    B1.value(1)
    utime.sleep_us(tempo)

    B2.value(0)
    utime.sleep_us(tempo)

    A2.value(1)
    utime.sleep_us(tempo)

    B1.value(0)
    utime.sleep_us(tempo)

    A1.value(1)
    utime.sleep_us(tempo)

    A2.value(0)
    utime.sleep_us(tempo)

    B2.value(1)
    utime.sleep_us(tempo)

    A1.value(0)
    B2.value(0)

def Rstep() :

    A1.value(1)
    utime.sleep_us(tempo)

    A2.value(1)
    utime.sleep_us(tempo)

    A1.value(0)
    utime.sleep_us(tempo)

    B1.value(1)
    utime.sleep_us(tempo)

    A2.value(0)
    utime.sleep_us(tempo)

    B2.value(1)
    utime.sleep_us(tempo)

    B1.value(0)
    utime.sleep_us(tempo)

    A1.value(1)
    utime.sleep_us(tempo)

    A1.value(0)
    B2.value(0)


def motor_off():
    A1.value(0)
    A2.value(0)
    B1.value(0)
    B2.value(0)

for o in range(3):
    for i in range(512):
        Rstep()

    for i in range(512):
        Lstep()

motor_off()
    
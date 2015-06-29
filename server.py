# BIG-BANG - TEACHER

# Import modules
import time
import RPi.GPIO as GPIO
import pygame

# GPIO pins on breadboard
INPUTS  = [5,6,7,8,9]
OUTPUTS = [10,11,12,13,14]
ARMED   = 15
BANG    = 16

# Setup
pygame.mixer.init()
bang = pygame.Sound("bang.wav")
GPIO.setmode(GPIO.BCM)
for i in INPUTS:
    GPIO.setup(i, GPIO.IN)
for o on OUTPUTS:
    GPIO.setup(o, GPIO.OUT)
    GPIO.output(o, False)
GPIO.setup(ARMED, GPIO.IN)

# Variables
ins = [False,False,False,False,False]
state = "MONITORING"

# Main loop
while True:
    time.sleep(1)

    # Sensing
    count = 0
    for i in range(len(INPUTS)):
        ins[i] = GPIO.input(INPUTS[i])
        if ins[i]:
            count += 1

    if state == "MONITORING":
        print("monitor:" + str(ins))
        if armed:
            state = "WAITING"

    elif state == "WAITING":
        if count < len(INPUTS)
            print("Still waiting:" + str(ins))
        else:
            state = "BANG"

    elif state == "BANG":
        print("firing...")
        count = 5
        for o in OUTPUTS:
            print("Bang! " + str(count))
            GPIO.output(o, True)
            time.sleep(0.5)
            GPIO.output(o, False)
            count -= 1

        print("BIG BANG!")
	GPIO.output(BANG, True)
        bang.play()
        time.sleep(5)
        GPIO.output(BANG, False)
        state = "FIRED"

    elif state == "FIRED":
        if count > 0 or armed:
            print("waiting for disarm:" + armed + " " + str(ins))
        else:
            state = "MONITORING"

# END
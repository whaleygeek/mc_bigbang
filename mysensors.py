# BIG BANG - STUDENT

# Import modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import RPi.GPIO as GPIO
####import pygame
import time


# GPIO pins on breadboard
BUTTON = 4
LED    = 15

# Setup
mc = minecraft.Minecraft.create()
GPIO.setmode(GPIO.BCM) # use broadcom GPIO numbers
GPIO.setup(BUTTON, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
####pygame.mixer.init()
####bang = pygame.mixer.Sound("explosion.wav")

mc.postToChat("Time to go mining!")

# Main loop
while True:
    time.sleep(0.1)

    # Sensing
    pos = mc.player.getTilePos()
    b = mc.getBlock(pos.x, pos.y, pos.z)
    button = not GPIO.input(BUTTON)

    # LED on, if standing on magic block
    if b == block.STONE.id:
        GPIO.output(LED, False)
    else:
        GPIO.output(LED, False)

    # big bang if button pressed
    if button:
        mc.postToChat("BANG!")
        ####bang.play()
        mc.player.setTilePos(pos.x, pos.y+20, pos.z) # send player up in sky!
        mc.setBlocks(pos.x-10, pos.y-1, pos.z-10, pos.x+10, pos.y+10, pos.z+10, block.AIR.id)

# END

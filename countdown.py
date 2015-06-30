# BIG BANG - COUNTDOWN

# Import modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
#import RPi.GPIO as GPIO
import anyio.GPIO as GPIO

# GPIO pins on breadboard
BANG    = 15

# Setup
mc = minecraft.Minecraft.create()
GPIO.setmode(GPIO.BCM) # use broadcom GPIO numbers
GPIO.setup(BANG, GPIO.OUT)

pos = mc.player.getTilePos()
mc.setBlock(pos.x+1, pos.y, pos.z, block.GOLD_BLOCK.id)
mc.postToChat("hit that gold block!")

# Main loop
while True:
    time.sleep(0.1)

    # Input Sensing
    bang = False
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        b = mc.getBlock(pos.x, pos.y, pos.z)
        bang = (b == block.GOLD_BLOCK.id)

    # Output Control
    if bang:
        for v in range(5,0,-1):
            mc.postToChat(str(v))
            time.sleep(1)
            
        mc.postToChat("BANG!")
        mc.setBlock(pos.x-10, pos.y-5, pos.z-10, pos.x+10, pos.y+10, pos.z+10, block.AIR.id)
        GPIO.output(BANG, True)
        time.sleep(3)
        GPIO.output(BANG, False)
        
# END

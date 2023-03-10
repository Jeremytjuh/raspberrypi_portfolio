import RPi.GPIO as GPIO
import time

outputPin = 3
lastTime = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(outputPin, GPIO.OUT)

# Geeft de tijd dat de applicatie draait terug in milliseconden
def millis():
    return time.time() * 1000

def loop():
    global lastTime
    # Als er 1000 milliseconden gepasseerd is sinds de laatste keer
    if millis() - lastTime >= 1000:
        lastTime = millis()
        if GPIO.input(outputPin):
            GPIO.output(outputPin, GPIO.LOW)
        else:
            GPIO.output(outputPin, GPIO.HIGH)

while True:
    loop()
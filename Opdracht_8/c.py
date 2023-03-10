import RPi.GPIO as GPIO
import time

# 3 input, 4 output
ardPins = [3, 4]
lastTime = 0
ledState = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(ardPins[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(ardPins[1], GPIO.OUT)

# Geeft de tijd dat de applicatie draait terug in milliseconden
def millis():
    return time.time() * 1000

while True:
    if GPIO.input(ardPins[0]):
        # Als er 1000 milliseconden gepasseerd is sinds de laatste keer dat de LED geknipperd heeft
        if millis() - lastTime >= 1000:
            lastTime = millis()
            if ledState:
                GPIO.output(ardPins[1], GPIO.HIGH)
                ledState = False
            else:
                GPIO.output(ardPins[1], GPIO.LOW)
                ledState = True

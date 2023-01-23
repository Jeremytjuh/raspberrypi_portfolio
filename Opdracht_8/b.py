import RPi.GPIO as GPIO
import time

outputPins = [3, 4]
lastTimes = [0, 0]
delays = [1000, 1000]

GPIO.setmode(GPIO.BCM)
for i in range(2):
    GPIO.setup(outputPins[i], GPIO.OUT)

def millis():
    return time.time() * 1000

def loop():
    global lastTimes
    for i in range(2):
        if millis() - lastTimes[i] >= delays[i]:
            lastTimes[i] = millis()
            if GPIO.input(outputPins[i]):
                GPIO.output(outputPins[i], GPIO.LOW)
            else:
                GPIO.output(outputPins[i], GPIO.HIGH)

while True:
    loop()

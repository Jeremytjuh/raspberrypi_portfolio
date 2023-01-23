import RPi.GPIO as GPIO
import time

ardPins = [11, 9, 10, 22]
outputPins = [26, 19, 13, 6]
lastTimes = [0, 0, 0, 0]
delays = [500, 500, 0, 0]
selectedLed = -1

GPIO.setmode(GPIO.BCM)
for i in range(4):
    GPIO.setup(ardPins[i], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
for i in range(4):
    GPIO.setup(outputPins[i], GPIO.OUT)

def millis():
    return time.time() * 1000

def setDelay(index, delay):
    delays[index] = delay

def checkForInput():
    global selectedLed
    for i in range(4):
        if GPIO.input(ardPins[i]):
            time.sleep(0.05)
            newI = i + 1
            if selectedLed == -1:
                selectedLed = i
            else:
                setDelay(selectedLed, newI * 100)
                selectedLed = -1

def loop():
    global lastTimes
    for i in range(4):
        if millis() - lastTimes[i] >= delays[i]:
            lastTimes[i] = millis()
            if GPIO.input(outputPins[i]):
                GPIO.output(outputPins[i], GPIO.LOW)
            else:
                GPIO.output(outputPins[i], GPIO.HIGH)

while True:
    checkForInput()
    loop()
import RPi.GPIO as GPIO
import time

LED_PINS = [22, 26]
BTN_PIN = 27
knipperTime = 1000
knipperTimePressed = 1300
lastTime = 0
ledStatus = [GPIO.LOW, GPIO.LOW]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PINS[0], GPIO.OUT)
GPIO.setup(LED_PINS[1], GPIO.OUT)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def millis():
    return time.time() * 1000

while True:
    currentTime = millis()
    if GPIO.input(BTN_PIN) == GPIO.HIGH:
        if currentTime - lastTime >= knipperTime:
            lastTime = currentTime
            if ledStatus[0] == GPIO.HIGH:
                ledStatus[0] = GPIO.LOW
                ledStatus[1] = GPIO.HIGH
            else:
                ledStatus[0] = GPIO.HIGH
                ledStatus[1] = GPIO.LOW
            for i in range(2):
                GPIO.output(LED_PINS[i], ledStatus[i])
    else:
        if currentTime - lastTime >= knipperTimePressed:
            lastTime = currentTime
            if ledStatus[0] == GPIO.HIGH:
                ledStatus[0] = GPIO.LOW
                ledStatus[1] = GPIO.HIGH

                knipperTimePressed = 700
            else:
                ledStatus[0] = GPIO.HIGH
                ledStatus[1] = GPIO.LOW

                knipperTimePressed = 1300
            for i in range(2):
                GPIO.output(LED_PINS[i], ledStatus[i])

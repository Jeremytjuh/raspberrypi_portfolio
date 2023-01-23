import RPi.GPIO as GPIO
import time

LED_PINS = [22, 26]
BTN_PINS = [27, 25]
knipperTimes = [1000, 1000]
lastTimes = [0, 0]
ledStatus = [GPIO.LOW, GPIO.LOW]

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PINS[0], GPIO.OUT)
GPIO.setup(LED_PINS[1], GPIO.OUT)
GPIO.setup(BTN_PINS[0], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_PINS[1], GPIO.IN, pull_up_down=GPIO.PUD_UP)

def millis():
    return time.time() * 1000

while True:
    currentTime = millis()
    for i in range(1):
        if GPIO.input(BTN_PINS[i]) == GPIO.HIGH:
            GPIO.output(LED_PINS[i], GPIO.LOW)
        else:
            if currentTime - lastTimes[i] >= knipperTimes[i]:
                lastTimes[i] = currentTime
                if ledStatus[i] == GPIO.HIGH:
                    ledStatus[i] = GPIO.LOW
                else:
                    ledStatus[i] = GPIO.HIGH
                GPIO.output(LED_PINS[i], ledStatus[i])
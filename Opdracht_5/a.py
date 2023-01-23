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

# Geeft de tijd dat de applicatie draait terug in milliseconden
def millis():
    return time.time() * 1000

while True:
    currentTime = millis()
    for i in range(1):
        # Als er niet op de knop geklikt wordt -> LED uit
        if GPIO.input(BTN_PINS[i]) == GPIO.HIGH:
            GPIO.output(LED_PINS[i], GPIO.LOW)
        # Als er wel op de knop geklikt wordt
        else:
            # Als er 1000 milliseconden gepasseerd is sinds de laatste keer dat de LED geknipperd heeft
            if currentTime - lastTimes[i] >= knipperTimes[i]:
                lastTimes[i] = currentTime
                # Als de led al aan stond -> zet hem uit
                if ledStatus[i] == GPIO.HIGH:
                    ledStatus[i] = GPIO.LOW
                # Als de led uit stond -> zet hem aan
                else:
                    ledStatus[i] = GPIO.HIGH
                GPIO.output(LED_PINS[i], ledStatus[i])
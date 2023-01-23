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

# Geeft de tijd dat de applicatie draait terug in milliseconden
def millis():
    return time.time() * 1000

while True:
    currentTime = millis()
    # Als er niet op de knop geklikt wordt
    if GPIO.input(BTN_PIN) == GPIO.HIGH:
        # Als er 1000 milliseconden gepasseerd is sinds de laatste keer dat de LED geknipperd heeft
        if currentTime - lastTime >= knipperTime:
            lastTime = currentTime
            # Als led 1 al aan stond -> zet hem uit en zet led 2 aan
            if ledStatus[0] == GPIO.HIGH:
                ledStatus[0] = GPIO.LOW
                ledStatus[1] = GPIO.HIGH
            # Als led 1 uit stond -> zet hem aan en zet led 2 uit
            else:
                ledStatus[0] = GPIO.HIGH
                ledStatus[1] = GPIO.LOW
            for i in range(2):
                GPIO.output(LED_PINS[i], ledStatus[i])
    else:
        # Als er een set aantal milliseconden gepasseerd is sinds de laatste keer dat de LED geknipperd heeft
        if currentTime - lastTime >= knipperTimePressed:
            lastTime = currentTime
            # Als led 1 al aan stond -> zet hem uit en zet led 2 aan
            if ledStatus[0] == GPIO.HIGH:
                ledStatus[0] = GPIO.LOW
                ledStatus[1] = GPIO.HIGH

                # Verander de knippertijd naar 700 milliseconden
                knipperTimePressed = 700
            # Als led 1 uit stond -> zet hem aan en zet led 2 uit
            else:
                ledStatus[0] = GPIO.HIGH
                ledStatus[1] = GPIO.LOW

                # Verander de knippertijd naar 1300 milliseconden
                knipperTimePressed = 1300
            for i in range(2):
                GPIO.output(LED_PINS[i], ledStatus[i])

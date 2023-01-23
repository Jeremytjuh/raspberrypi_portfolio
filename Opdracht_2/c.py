import RPi.GPIO as GPIO
import time

# GPIO Pin waarop de LED is aangesloten
LED_PIN = 16

# Configureren van de Raspberry Pi voor het gebruik van de GPIO pins
GPIO.setmode(GPIO.BCM)
# Instellen van de pin als uitvoer in plaats van invoer
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    # Aanzetten van de LED
    GPIO.output(LED_PIN, GPIO.HIGH)
    # Delay van 0.1 seconden
    time.sleep(0.1)
    # Uitzetten van de LED
    GPIO.output(LED_PIN, GPIO.LOW)
    # Delay van 0.1 seconden
    time.sleep(0.1)
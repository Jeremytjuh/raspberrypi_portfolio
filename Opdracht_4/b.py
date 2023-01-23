import RPi.GPIO as GPIO
import time

LED_PIN1 = 22
LED_PIN2 = 26
BTN_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    if GPIO.input(BTN_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN2, GPIO.LOW)
    else:
        GPIO.output(LED_PIN2, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN2, GPIO.LOW)
        time.sleep(1)
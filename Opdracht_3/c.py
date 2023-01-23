import RPi.GPIO as GPIO
import time

LED_PIN1 = 22
LED_PIN2 = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

while True:
    GPIO.output(LED_PIN1, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(LED_PIN1, GPIO.LOW)
    time.sleep(0.7)
    GPIO.output(LED_PIN2, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(LED_PIN2, GPIO.LOW)
    time.sleep(1.7)

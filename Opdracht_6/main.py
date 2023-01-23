import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# Servo setup, aangesloten op pin 6
SERVO_PIN = 6
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(0)
# Button setup, aangesloten op pins 9 & 4
BUTTON_PIN1 = 9
BUTTON_PIN2 = 4
GPIO.setup(BUTTON_PIN1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, GPIO.PUD_UP)

def millis():
    return time.time() * 1000

# Functie servo hoek aanpassen
def SetAngle(angle, delay):
    cycle = angle / 18 + 2
    pwm.ChangeDutyCycle(cycle)
    time.sleep(delay)
    pwm.ChangeDutyCycle(0)

while True:
    # Zodra er op Button 1 gedrukt wordt -> draaien hoek servomotor van 0 naar 120 graden binnen 1 seconden
    if GPIO.input(BUTTON_PIN1) == GPIO.LOW:
        SetAngle(0, 1)
        SetAngle(120, 1)

    # Zodra er op Button 2 gedrukt wordt -> draaien hoek servomotor van 0 naar 120 graden binnen 0.5 seconden
    if GPIO.input(BUTTON_PIN2) == GPIO.LOW:
        SetAngle(0, 0.5)
        SetAngle(120, 0.5)
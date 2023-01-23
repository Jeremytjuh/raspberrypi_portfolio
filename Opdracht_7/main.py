import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib

GPIO.setmode(GPIO.BCM)
# Setup DC Motor, aangesloten op GPIO pins 19, 13, 5 & 10
DCMOTOR_PINS = [19, 13, 5, 10]
motor = RpiMotorLib.BYJMotor("Motortje", "28BYJ")

# Setup Buttons, aangesloten op GPIO pins 9 & 4
BUTTON_PIN1 = 9
BUTTON_PIN2 = 4
GPIO.setup(BUTTON_PIN1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN2, GPIO.IN, GPIO.PUD_UP)

try:
    while True:
        # Zodra er op Button 1 gedrukt wordt -> draait linksom binnen 5 seconden
        if GPIO.input(BUTTON_PIN1) == GPIO.LOW:
            # 1 ronde bestaat uit 512 stappen, 5 (seconden) / 512 (stappen) ≈ 0.01 (seconde per stap)
            # 4e parameter op False -> linksom draaien
            motor.motor_run(DCMOTOR_PINS, .001, 100, False, False, "half", 0)

        # Zodra er op Button 2 gedrukt wordt -> draait rechtsom binnen 12 seconden
        if GPIO.input(BUTTON_PIN2) == GPIO.LOW:
            # 1 ronde bestaat uit 512 stappen, 12 (seconden) / 512 (stappen) ≈ 0.0234 (seconde per stap)
            # 4e parameter op True -> rechtsom draaien
            motor.motor_run(DCMOTOR_PINS, .00234, 100, True, False, "half", 0)

finally:
    # Leegmaken GPIO pins
    GPIO.cleanup()
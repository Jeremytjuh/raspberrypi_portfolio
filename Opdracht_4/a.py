import RPi.GPIO as GPIO

LED_PIN1 = 22
LED_PIN2 = 26
BTN_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)
# Instellen button pin als input, ik gebruik PUD_UP omdat ik anders problemen kreeg
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    # Als er niet op de knop geklikt wordt -> zet dan de LED aan, anders uit
    if GPIO.input(BTN_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN2, GPIO.LOW)
    else:
        GPIO.output(LED_PIN2, GPIO.HIGH)
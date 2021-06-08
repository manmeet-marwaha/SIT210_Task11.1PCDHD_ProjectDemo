import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 21
ECHO = 20
buzzer = 16
print(" Distance Measurement in progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)


while True:
    GPIO.output(TRIG, False)

    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.01)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start=time.time()

    while GPIO.input(ECHO)==1:
        pulse_end=time.time()

    pulse_duration = pulse_end-pulse_start

    distance = pulse_duration*11150
    distance = round(distance,2)

    if distance > 20:
        GPIO.output(buzzer, GPIO.LOW)
        print("BUZZER OFF")
    else:
        print("BUZZER ON")
        GPIO.output(buzzer, GPIO.HIGH)
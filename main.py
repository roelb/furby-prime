import RPi.GPIO as GPIO
from time import sleep

FURB_PIN_TILT = 17
FURB_PIN_MOTOR_FWD = 27
FURB_PIN_MOTOR_BCK = 22
FURB_PIN_UPSIDE_DOWN = 5
FURB_PIN_CAM_HOME = 6
FURB_PIN_GEAR_ROT = 26
FURB_PIN_TUMMY = 23
FURB_PIN_RESET = 24 
FURB_PIN_BACK = 25
FURB_PIN_LIGHT_IN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(FURB_PIN_MOTOR_FWD,GPIO.OUT)
GPIO.setup(FURB_PIN_RESET, GPIO.IN)

GPIO.output(FURB_PIN_MOTOR_FWD, GPIO.HIGH)

sleep(5)

print("start")
while True:
    

    while not GPIO.input(FURB_PIN_RESET):
        print("reset pressed")
        GPIO.output(FURB_PIN_MOTOR_FWD, GPIO.HIGH)
        sleep(0.1)
    print("reset not pressed")
    GPIO.output(FURB_PIN_MOTOR_FWD, GPIO.LOW)
    sleep(0.1)

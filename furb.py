import RPi.GPIO as GPIO
from time import sleep


"""
Pinout:
    1. TILT
    2. Motor forward black
    3. Upside down
    4. Power down
    5. IR in
    6. /CAM home white
    7. Light in
    8. 6V
    9. Serial out
    10. Gear Rotation grey
    11. Speaker +
    12. Motor reverse purple
    13. Serial in
    14. Ground
    15. Tummy
    16. Serial clock
    17. IR out
    18. Reset red
    19. /Back
    20. Speaker -
    21. Gear LED brown
"""

FURB_PIN_TILT = 17
FURB_PIN_MOTOR_FWD = 27
FURB_PIN_MOTOR_REV = 22
FURB_PIN_UPSIDE_DOWN = 5
FURB_PIN_CAM_HOME = 6
FURB_PIN_GEAR_ROT = 26
FURB_PIN_TUMMY = 23
FURB_PIN_RESET = 24
FURB_PIN_BACK = 25
FURB_PIN_LIGHT_IN = 16


MOTOR_FWD = 1
MOTOR_REV = -1
MOTOR_STP = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(FURB_PIN_MOTOR_FWD, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(FURB_PIN_MOTOR_REV, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(FURB_PIN_RESET, GPIO.IN)

GPIO.setup(FURB_PIN_CAM_HOME, GPIO.IN)
GPIO.setup(FURB_PIN_GEAR_ROT, GPIO.IN)


def log(message: str = ""):
    print(f"[i] {message}") 
def warn(message: str = ""):
    print(f"[w] {message}")


def write_motor(direction: int):
    # direction: 0 -> stop, -1 -> reverse, 1 -> forward
    if direction == -1:
        GPIO.output(FURB_PIN_MOTOR_FWD, GPIO.LOW)
        GPIO.output(FURB_PIN_MOTOR_REV, GPIO.HIGH)
    elif direction == 1:
        GPIO.output(FURB_PIN_MOTOR_REV, GPIO.LOW)
        GPIO.output(FURB_PIN_MOTOR_FWD, GPIO.HIGH)
    elif direction == 0:
        GPIO.output(FURB_PIN_MOTOR_REV, GPIO.LOW)
        GPIO.output(FURB_PIN_MOTOR_FWD, GPIO.LOW)
 
def read_reset():
    return GPIO.input(FURB_PIN_RESET)
def read_cam_home():
    return GPIO.input(FURB_PIN_CAM_HOME)
def read_gear_rot():
    return GPIO.input(FURB_PIN_GEAR_ROT)

def motor_fwd_until_rot():
    write_motor(MOTOR_FWD)
    while not read_gear_rot():
        pass
    print(read_gear_rot())
    write_motor(MOTOR_STP)

def motor_fwd_until_home(direction=MOTOR_FWD):
    count = 0
    write_motor(direction)
    while True:
        sleep(0.01)
        if read_cam_home() == 0:
            count += 1
        else:
            count = 0

        if count > 1:
            #print("cam home: " + str(read_cam_home()))
            write_motor(MOTOR_STP)
            break
def espeak():
	import os
	os.system("""espeak -p10 'A balanced output allows the device to sink and source similar currents. The drive capability of this device
	may create fast edges into light loads so routing and load conditions should be considered to prevent ringing.
	Additionally, the outputs of this device are capable of driving larger currents than the device can sustain without
	being damaged. It is important for the output power of the device to be limited to avoid damage due to
	over-current. The electrical and thermal limits defined in the Absolute Maximum Ratings must be followed at all
	times.'""")
 

def speak0(time):
    write_motor(MOTOR_STP)
    write_motor(MOTOR_REV)
    sleep(0.2)
    write_motor(MOTOR_STP)
    motor_fwd_until_home(MOTOR_FWD)
    write_motor(MOTOR_FWD)
    sleep(0.7)
    write_motor(MOTOR_STP)
    motor_fwd_until_home(MOTOR_REV)

def speak1(time):
    write_motor(MOTOR_STP)
    write_motor(MOTOR_FWD)
    sleep(0.7)
    write_motor(MOTOR_STP)
    motor_fwd_until_home(MOTOR_REV)
    return
    write_motor(MOTOR_REV)
    sleep(0.7)
    write_motor(MOTOR_STP)
    motor_fwd_until_home(MOTOR_FWD)
    return
def speak2(time):
    while True:
        print("loop")
        speak0(0)
        speak0(0)
        speak0(0)
        speak1(0)
        speak0(0)
        speak0(0)
        speak1(0)

def main():
    sleep(2)
    #write_motor(MOTOR_FWD)
    count = 0

    log("waiting for reset")
    while read_reset():
        sleep(0.2)

    log("reset pressed")
    log("waiting for reset")

    while True:
        while read_reset():
            pass
        motor_fwd_until_home()
        sleep(1)
        import threading
        x = threading.Thread(target=espeak, args=())
        x.start()
        speak2(0)
        write_motor(MOTOR_STP)
        return


if __name__ == "__main__":
    main()

def thread_function(name):

    logging.info("Thread %s: starting", name)

    time.sleep(2)

    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    logging.basicConfig(format=format, level=logging.INFO,

                        datefmt="%H:%M:%S")
    logging.info("Main    : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")

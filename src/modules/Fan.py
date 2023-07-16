from enum import Enum
from gpiozero import LED
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)
fan_speed = GPIO.PWM(24, 100)
fan_power_switch = LED(11)
fan_speed.start(0)


class FanStatus(Enum):
    STOP = 0
    MEDIUM = 1
    HIGH = 2


class Fan:
    current_status = FanStatus.STOP

    def start_high(self):
        if self.current_status != FanStatus.HIGH:
            print("Starting fan - High")
            fan_speed.ChangeDutyCycle(100)
            fan_power_switch.on()
            self.current_status = FanStatus.HIGH

    def start_medium(self):
        if self.current_status != FanStatus.MEDIUM:
            print("Starting fan - Medium")
            fan_speed.ChangeDutyCycle(50)
            fan_power_switch.on()
            self.current_status = FanStatus.MEDIUM

    def stop(self):
        if self.current_status != FanStatus.STOP:
            print("Stopping fan")
            fan_power_switch.off()
            fan_speed.ChangeDutyCycle(0)
            self.current_status = FanStatus.STOP

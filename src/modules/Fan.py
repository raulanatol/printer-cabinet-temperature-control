from enum import Enum
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)
fan = GPIO.PWM(24, 100)
fan.start(0)


class FanStatus(Enum):
    STOP = 0
    MEDIUM = 1
    HIGH = 2


class Fan:
    current_status = FanStatus.STOP

    def start_high(self):
        if self.current_status != FanStatus.HIGH:
            print("Starting fan - High")
            fan.ChangeDutyCycle(100)
            self.current_status = FanStatus.HIGH

    def start_medium(self):
        if self.current_status != FanStatus.MEDIUM:
            print("Starting fan - Medium")
            fan.ChangeDutyCycle(50)
            self.current_status = FanStatus.MEDIUM

    def stop(self):
        if self.current_status != FanStatus.STOP:
            print("Stopping fan")
            fan.ChangeDutyCycle(0)
            self.current_status = FanStatus.STOP

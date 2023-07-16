from enum import Enum
import RPi.GPIO as GPIO

fan_speed_pin = 8
fan_power_switch_pin = 17

GPIO.setup(fan_speed_pin, GPIO.OUT)
GPIO.setup(fan_power_switch_pin, GPIO.OUT, initial=GPIO.LOW)

fan_speed = GPIO.PWM(fan_speed_pin, 100)
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
            GPIO.output(fan_power_switch_pin, GPIO.HIGH)
            self.current_status = FanStatus.HIGH

    def start_medium(self):
        if self.current_status != FanStatus.MEDIUM:
            print("Starting fan - Medium")
            fan_speed.ChangeDutyCycle(50)
            GPIO.output(fan_power_switch_pin, GPIO.HIGH)
            self.current_status = FanStatus.MEDIUM

    def stop(self):
        if self.current_status != FanStatus.STOP:
            print("Stopping fan")
            GPIO.output(fan_power_switch_pin, GPIO.LOW)
            fan_speed.ChangeDutyCycle(0)
            self.current_status = FanStatus.STOP

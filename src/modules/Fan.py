from enum import Enum
from gpiozero import LED

fan = LED(11)

class FanStatus(Enum):
    STOP = 0
    MEDIUM = 1
    HIGH = 2


class Fan:
    current_status = FanStatus.STOP

    def start_high(self):
        if self.current_status != FanStatus.HIGH:
            print("Starting fan - High")
            fan.on()
            self.current_status = FanStatus.HIGH

    def start_medium(self):
        if self.current_status != FanStatus.MEDIUM:
            print("Starting fan - Medium")
            fan.on()
            self.current_status = FanStatus.MEDIUM

    def stop(self):
        if self.current_status != FanStatus.STOP:
            print("Stopping fan")
            fan.off()
            self.current_status = FanStatus.STOP

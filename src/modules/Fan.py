import RPi.GPIO as GPIO

fan_power_switch_pin = 17

GPIO.setup(fan_power_switch_pin, GPIO.OUT, initial=GPIO.LOW)

class Fan:
    is_running = False\

    def stop(self):
        if self.is_running:
            print("Stopping fan")
            GPIO.output(fan_power_switch_pin, GPIO.LOW)
            self.is_running = False

    def start(self):
        if not self.is_running:
        print("Starting fan")
        GPIO.output(fan_power_switch_pin, GPIO.HIGH)
        self.is_running = True

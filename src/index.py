#!/usr/bin/python
import RPi.GPIO as GPIO
import board

from time import sleep
from modules.TemperatureSensor import TemperatureSensor
from modules.LCD import LCD
from modules.Fan import Fan, FanStatus

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# ----
TEMPERATURE_SENSOR_PORT = 4
MEDIUM_TEMPERATURE = 25
HIGH_TEMPERATURE = 30
# ----

# Start modules
temperatureSensor = TemperatureSensor(board.D4)
lcd = LCD()
fan = Fan()


def print_measurement():
    temperature_word = 'Temperature = {0:0.1f}*C'.format(temperatureSensor.temperature)
    humidity_word = 'Humidity = {0:0.1f}%'.format(temperatureSensor.humidity)
    print(temperature_word)
    print(humidity_word)
    print('===================')
    lcd.clear()
    lcd.draw_string(temperature_word, 1)
    lcd.draw_string(humidity_word, 2)


def control_threshold():
    if temperatureSensor.temperature > HIGH_TEMPERATURE:
        fan.start_high()
        lcd.clear()
        lcd.draw_string('Starting fan HIGH', 1)
        return

    if temperatureSensor.temperature > MEDIUM_TEMPERATURE:
        fan.start_medium()
        lcd.clear()
        lcd.draw_string('Starting fan MEDIUM', 1)
        return

    if fan.current_status != FanStatus.STOP:
        fan.stop()
        lcd.clear()
        lcd.draw_string('Stopping fan', 1)


def main():
    try:
        while True:
            temperatureSensor.read()
            print_measurement()
            control_threshold()
            sleep(5)
    except KeyboardInterrupt as e:
        print("Stopping...")
        temperatureSensor.exit()


main()

#!/usr/bin/python
import RPi.GPIO as GPIO
import board

from time import sleep
from modules.TemperatureSensor import TemperatureSensor
from modules.LCD import LCD
from modules.Fan import Fan

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ----
TEMPERATURE_SENSOR_PORT = 4
UPPER_THRESHOLD = 40
LOWER_THRESHOLD = 30

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
    if temperatureSensor.temperature > UPPER_THRESHOLD:
        if not fan.is_running:
            fan.start()
            lcd.clear()
            lcd.draw_string('Starting fan', 1)
        return

    if temperatureSensor.temperature < LOWER_THRESHOLD:
        if fan.is_running:
            fan.stop()
            lcd.clear()
            lcd.draw_string('Stopping fan', 1)
        return


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
        fan.stop()


main()

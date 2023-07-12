#!/usr/bin/python
from time import sleep

from modules.TemperatureSensor import TemperatureSensor
from modules.LCD import LCD
from modules.Fan import Fan

# ----
TEMPERATURE_SENSOR_PORT = 4
MEDIUM_TEMPERATURE = 25
HIGH_TEMPERATURE = 30
# ----

# Start modules
temperatureSensor = TemperatureSensor(4)
lcd = LCD()
fan = Fan()


def print_measurement():
    temperature_word = 'Temperature = {0:0.1f}*C'.format(temperatureSensor.temperature)
    humidity_word = 'Humidity = {0:0.1f}%'.format(temperatureSensor.humidity)
    print(temperature_word)
    print(humidity_word)
    print('===================')
    lcd.draw_string(temperature_word, 0, 0)
    lcd.draw_string(humidity_word, 0, 0)


def control_threshold():
    if temperatureSensor.temperature > HIGH_TEMPERATURE:
        fan.start_high()
        lcd.draw_string('Starting fan HIGH', 0, 0)
        return

    if temperatureSensor.temperature > MEDIUM_TEMPERATURE:
        fan.start_medium()
        lcd.draw_string('Starting fan MEDIUM', 0, 0)
        return

    fan.stop()
    lcd.draw_string('Stopping fan', 0, 0)


def main():
    try:
        while True:
            temperatureSensor.read()
            print_measurement()
            control_threshold()
            sleep(5)
    except KeyboardInterrupt as e:
        print("Stopping...")


main()

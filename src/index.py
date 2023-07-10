#!/usr/bin/python
from time import sleep
from TemperatureSensor import TemperatureSensor

sensor = TemperatureSensor(4)

try:
    while True:
        sensor.read()
        print('Temperature = {0:0.1f}*C'.format(sensor.temperature))
        print('Humidity    = {0:0.1f}%'.format(sensor.humidity))
        print('===================')
        sleep(5)
except KeyboardInterrupt as e:
    print("Stopping...")
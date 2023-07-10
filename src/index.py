#!/usr/bin/python
from time import sleep

try:
    while True:
        print("Hello world")
        sleep(60)
except KeyboardInterrupt as e:
    print("Stopping...")
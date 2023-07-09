import Adafruit_DHT as dht
from time import sleep

# Data pin number. Eg: 4
DHT = 4

while True:
    humidity,temperature = dht.read_retry(dht.DHT22, DHT)

    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
    sleep(5)


import Adafruit_DHT as dht


class TemperatureSensor:
    """The DHT sensor"""
    port = 4
    humidity = 0
    temperature = 0

    def __init__(self, port):
        self.port = port

    def read(self):
        humidity, temperature = dht.read_retry(dht.DHT22, self.port)
        self.humidity = humidity
        self.temperature = temperature

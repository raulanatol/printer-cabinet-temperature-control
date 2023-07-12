import Adafruit_DHT as dht


class TemperatureSensor:
    """The DHT sensor"""
    port = 4
    humidity = None
    temperature = None

    def __init__(self, port):
        self.port = port

    def read(self):
        humidity, temperature = dht.read_retry(dht.DHT22, self.port)
        # humidity = 12
        # temperature = 20
        self.humidity = humidity
        self.temperature = temperature

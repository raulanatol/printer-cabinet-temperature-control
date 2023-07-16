import adafruit_dht

class TemperatureSensor:
    """The DHT sensor"""
    sensor = None
    port = 4
    humidity = 0
    temperature = 0

    def __init__(self, port):
        self.sensor = adafruit_dht.DHT22(port, use_pulseio=True)
        self.port = port

    def read(self):
        try:
            self.temperature = self.sensor.temperature
            self.humidity = self.sensor.humidity
        except RuntimeError:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print("-")

    def exit(self):
        self.sensor.exit()

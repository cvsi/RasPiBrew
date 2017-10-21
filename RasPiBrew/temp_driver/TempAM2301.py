from RasPiBrew.Adafruit_Python_DHT import Adafruit_DHT

from RasPiBrew.temp_driver.AbstractSenor import AbstractSensor


class TempAM2301(AbstractSensor):
    numSensor = 0

    def __init__(self, sensor_id, pin_number):
        self.sensor_id = sensor_id
        self.gpio_data_pin = pin_number

    def read_temperature_c(self):
        humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, self.gpio_data_pin)

        return humidity, temp_c

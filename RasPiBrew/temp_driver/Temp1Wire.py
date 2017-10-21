from subprocess import Popen, PIPE
import os

from RasPiBrew.temp_driver.AbstractSenor import AbstractSensor


class Temp1Wire(AbstractSensor):
    numSensor = 0

    def __init__(self, temperature_sensor_id):
        self.tempSensorId = temperature_sensor_id
        self.sensorNum = Temp1Wire.numSensor
        Temp1Wire.numSensor += 1
        # Raspbian build in January 2015 (kernel 3.18.8 and higher) has changed the device tree.
        oldOneWireDir = "/sys/bus/w1/devices/w1_bus_master1/"
        newOneWireDir = "/sys/bus/w1/devices/"
        if os.path.exists(oldOneWireDir):
            self.oneWireDir = oldOneWireDir
        else:
            self.oneWireDir = newOneWireDir
        print("Constructing 1W sensor %s" % temperature_sensor_id)

    def read_temperature_c(self):
        pipe = Popen(["cat", self.oneWireDir + self.tempSensorId + "/w1_slave"], stdout=PIPE)

        result = pipe.communicate()[0]
        if result.split('\n')[0].split(' ')[11] == "YES":
            temp_C = float(result.split("=")[-1]) / 1000  # temp in Celcius
        else:
            temp_C = -99  # bad temp reading

        return temp_C

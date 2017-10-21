class AbstractSensor(object):

    def read_temperature_c(self):
        raise NotImplementedError("Should have implemented this")

import ljtemp
import probes
import zwave

import devices

class Brewery:

    def __init__(self):
        # LJTemp
        self.ljt = ljtemp.LJTemp()
        #self.ljt.connect()
        probe = probes.TemperatureProbe(name='R0', kind='RTD', model='pt1000',
                                        plus_input='AIN0', minus_input='GND')
        self.ljt.add_probe(probe)
        self.heater = devices.ZWaveBinarySwitch(name='heater', device_id=2, state='off')

    def heat(self, value):
        self.heater.set(value)

    def is_heating(self):
        return self.heater.is_on()

    def temperatures(self):
        """ Return all temperatures

        Return: array of dicts with 'name' and 'temp' in Celsiud
        """
        temps = []
        for probe in self.ljt.probes:
            temp = {
                'name': probe.name,
                'temperature': self.ljt.temperature_of_probe(probe)
            }
            temps.append(temp)
        return temps

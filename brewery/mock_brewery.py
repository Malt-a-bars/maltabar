from LJTemp import probes
import random


class Brewery:

    def __init__(self):
        self._probes = []
        probe = probes.TemperatureProbe(name='R0', kind='RTD', model='pt1000',
                                        plus_input='AIN0', minus_input='GND')
        self._probes.append(probe)

    def temperatures(self):
        """ Return all temperatures

        Return: array of dicts with 'name' and 'temp' in Celsius
        """
        temps = []
        for probe in self._probes:
            temp = {
                'name': probe.name,
                'temperature': self.temperature_of_probe(probe)
            }
            temps.append(temp)
        return temps

    def temperature_of_probe(self, probe):
        """ Return random temperatures """
        probe._mock_temp += random.random()  * 5- 2.5
        return probe._mock_temp

""" Control z-wave devices using a zwave-me raspberry pi extension """

# curl 'http://pi.local:8083/ZWaveAPI/Run/devices\[2\].instances\[0\].commandClasses\[0x25\].Set(255)' -X POST

import requests

class ZWave:

    def __init__(self, api_url='http://pi.local:8083/ZWaveAPI'):
        self.api_url = api_url

    def set_state(self, device_id, state):
        if state == 'on':
            value = 255
        elif state == 'off':
            value = 0
        else:
            raise TypeError("Invalid state {}, should be 'on' or 'off'.".format(state))
        url = "{0}/Run/devices[{1}].instances[0].commandClasses[0x25].Set({2})".format(self.api_url, device_id, value)
        print "Zwave set calling url: {}".format(url)
        r = requests.post(url)
        r.raise_for_status()

    def get_state(self, device_id):
        raise "Not implemented"
        # url = "{0}/Run/devices[{1}].instances[0].commandClasses[0x25].Set({2})".format(self.api_url, device_id, value)
        # print "Zwave set calling url: {}".format(url)
        # r = requests.post(url)
        # r.raise_for_status()

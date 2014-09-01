# class BinarySwitch:
#     """ Generic On/Off switch """
#     def __init__(self, name, state='off'):
#         self.name = name
#         self.state = state

#     def state(self):
#       print "BinarySwitch: Returning state {} for switch {}".format(self.state, self.name)
#       return self.state

#     def is_on(self):
#       value = (self.state == 'on')
#       print "BinarySwitch: Returning boolean value {} for switch {}".format(value, self.name)
#       return value

#     def set(self, state):
#       if state not in ['on', 'off']:
#           raise TypeError("BinarySwitch: Unknown state {}, should be 'on' or 'off'".format(state))
#       print "BinarySwitch: Setting state {} for switch {}".format(state, self.name)
#       self.state = state


import zwave


class ZWaveBinarySwitch:
    """ On/Off switch implemented using zwave """

    def __init__(self, name, device_id, state=''):
        self._name = name
        self._zw = zwave.ZWave()
        self._device_id = device_id

        if state == '':
            self._state = self.zw.get_state(device_id)
        else:
            self._zw.set_state(device_id, state)
            self._state = state

    def state(self):
        # TODO: get this from zwave
        value = self._state
        print "ZwaveBinarySwitch: Returning state {} for switch {}".format(value, self._name)
        return value

    def is_on(self):
        value = (self.state() == 'on')
        print "BinarySwitch: Returning boolean value {} for switch {}".format(value, self._name)
        return value

    def set(self, state):
        if state not in ['on', 'off']:
            raise TypeError("BinarySwitch: Unknown state {}, should be 'on' or 'off'".format(state))
        print "BinarySwitch: Setting state {} for switch {}".format(state, self._name)
        self._zw.set_state(self._device_id, state)
        self._state = state

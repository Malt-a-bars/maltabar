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
        # initialize self._state
        if state == '':
            self.state()
        else:
            self.set(state)

    def state(self):
        """ Refresh state from zwave and return it """
        self._state = self._zw.get_state(self._device_id)
        print "ZwaveBinarySwitch: Returning state {} for switch {}".format(self._state, self._name)
        return self._state

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

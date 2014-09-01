import unittest
import types
import zwave

class TestZwave(unittest.TestCase):

    def setUp(self):
        self.zw = zwave.ZWave()

    def tearDown(self):
        pass

    def test_set_on(self):
        self.zw.set_state(2, 'on')

    def test_set_off(self):
        self.zw.set_state(2, 'off')

if __name__ == '__main__':
    unittest.main()

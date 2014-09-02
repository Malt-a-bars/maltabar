import unittest
import types


class TestBrewery(unittest.TestCase):

    def setUp(self):
        #import mock_brewery as brewery
        import brewery
        self.brewery = brewery.Brewery()

    def tearDown(self):
        pass

    def test_read_temps(self):
        # read all temperatures
        temps = self.brewery.temperatures()
        self.assertEqual(type(temps), types.ListType, "temps should be a List")


if __name__ == '__main__':
    unittest.main()

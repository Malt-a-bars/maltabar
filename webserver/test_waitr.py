""" Test suite for the maltabar 'waitr' web API """

import unittest
import waitr
import json

API = '/api/v1'


class TestProbes(unittest.TestCase):

    def setUp(self):
        waitr.app.config['TESTING'] = True
        self.app = waitr.app.test_client()
        self.app.debug = True

    def test_get_probes(self):
        rv = self.app.get(API + '/probes')
        self.assertEqual(rv.status_code, 200, 'got: ' + rv.status)
        data = json.loads(rv.data)
        assert 'probes' in data


if __name__ == '__main__':
    unittest.main()

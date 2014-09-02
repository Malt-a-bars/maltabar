#!/usr/bin/env python
"""
waitr.py
Webserver for the maltabar brewery

Sam Grimee

Drink responsibly.
"""

#import mock_brewery as brewery
import brewery
import redis
import flask
import json
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

# configuration
DEBUG = True
API = '/api/v1'


class BreweryApp(flask.Flask):
    def __init__(self, import_name):
        super(BreweryApp, self).__init__(import_name)

        # Make error handlers return json
        for code in default_exceptions.iterkeys():
            self.error_handler_spec[None][code] = self.make_json_error

        self.red = redis.StrictRedis()

        # Initialise brewery
        self.brewery = brewery.Brewery()

        # configure all routes
        self.route(API+"/probes")(self.all_probes)

        self.route(API+"/is_heating")(self.is_heating)
        self.route(API+"/heater/<value>")(self.set_heater)

        self.route(API+"/stream")(self.stream)
        self.route(API+"/stream/update")(self.stream_update)
        self.route('/ui/<path:path>')(self.static_from_root)
        self.route('/')(self.redirect_to_ui)

    def all_probes(self):
        probes = self.brewery.temperatures()
        return flask.jsonify(probes=probes)

    def is_heating(self):
        value = self.brewery.is_heating()
        return flask.jsonify(value=value)

    def set_heater(self, value):
        self.brewery.heat(value)
        return 'heater value set to {}'.format(value)

    def make_json_error(self, ex):
            """ Handler that returns errors as json objects """
            response = flask.jsonify(message=str(ex))
            response.status_code = (ex.code if isinstance(ex, HTTPException)
                                    else 500)
            return response

    def event_stream(self):
        pubsub = self.red.pubsub()
        pubsub.subscribe('temperatures')

        # TODO: handle client disconnection.
        for message in pubsub.listen():
            print "Message: {0}".format(message)
            if message['type'] != 'message':
                continue
            data = json.dumps({message['channel']: json.loads(message['data'])})
            print "yielding data: {0}".format(data)
            yield "data: {0}\n\n".format(data)

    def stream(self):
        return flask.Response(self.event_stream(),
                              mimetype="text/event-stream")

    def stream_update(self):
        probes = self.brewery.temperatures()
        self.red.publish('temperatures', json.dumps(probes))
        return 'Stream updated'


    def static_from_root(self, path):
        print "path: {0}".format(path)
        return flask.send_from_directory('../../ui/dist', path)

    def redirect_to_ui(self):
        return flask.redirect('/ui/index.html')

app = BreweryApp(__name__)


if __name__ == '__main__':
    app.debug = True
    # reloader causes labjack connection issues
    app.run(host='0.0.0.0', use_reloader=False, threaded=True)

"""
waitr.py
Webserver for the maltabar brewery

Sam Grimee

Drink responsibly.
"""

from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

__all__ = ['make_json_app']

# configuration
DEBUG = True
API = '/api/v1'


# create application
def make_json_app(import_name, **kwargs):
    """
    Creates a JSON-oriented Flask app.

    All error responses that you don't specifically
    manage yourself will have application/json content
    type, and will contain JSON like this (just an example):

    { "message": "405: Method Not Allowed" }
    """
    def make_json_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (ex.code
                                if isinstance(ex, HTTPException)
                                else 500)
        return response

    app = Flask(import_name, **kwargs)

    for code in default_exceptions.iterkeys():
        app.error_handler_spec[None][code] = make_json_error

    return app

app = make_json_app(__name__)
app.config.from_object(__name__)
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)


@app.route(API + '/probes')
def all_probes():
    probes = [{'name': 'temp1',
               'value': 22.1,
               'unit': 'celsius'}]
    return jsonify(probes=probes)

if __name__ == '__main__':
    app.run()

#!/usr/bin/env python
""" Dummy webservice that returns random values

Arguments:
    optional port number

Example:
    python webservice-dummy.py 9080
"""

import web	# http://webpy.org
import random
import json

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        random_temp = random.random()
        temps = {'rand': random_temp}
        return json.dumps(random_temp * 100)

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()   

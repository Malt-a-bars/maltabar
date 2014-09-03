Waitr
=====

Web service for the brewery.

Run it with ```python -m waitr```

You must have a redis server running on localhost port 6379 for streaming support.

By default the HTTP webservice runs on TCP port 5000.
If you GET / you will be redirected to the UI.


API
---

prefix: /api/v1

GET  /heater/on  - turn heater on
GET  /heater/off - turn heater off
GET  /is_heating - returns a boolean indicating is the heater is turned on

GET  /probes - returns an array with all probes

GET  /stream - get an event stream with temperatures updates
GET  /stream/update - trigger the publication of a new temperature to the stream


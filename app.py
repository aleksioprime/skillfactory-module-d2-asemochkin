import sentry_sdk

import os
from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://f7a65db35ea04b4fafb93135404a9465@o514688.ingest.sentry.io/5618301",
    integrations=[BottleIntegration()]
)

@route('/')  
def index():  
    return "Hello World!"


@route('/success')  
def success():  
    return "200 OK"

@route('/fail')  
def error():  
    raise RuntimeError("There is an my error!")  
    return  

port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port)
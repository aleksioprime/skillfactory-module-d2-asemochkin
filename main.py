import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://f7a65db35ea04b4fafb93135404a9465@o514688.ingest.sentry.io/5618301",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/')  
def index():  
    return "Hello World!"


@app.route('/success')  
def success():  
    return "Success!"

@app.route('/fail')  
def error():  
    raise RuntimeError("There is an my error!")  
    return  
  
run(host='0.0.0.0')
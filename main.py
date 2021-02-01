import sentry_sdk

from bottle import Bottle, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://f7a65db35ea04b4fafb93135404a9465@o514688.ingest.sentry.io/5618301",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route('/success')  
def success():  
    return "Hello World!"

@app.route('/fail')  
def error():  
    raise RuntimeError("There is an error!")  
    return  
  
  
app.run(host='practice-semochkin.herokuapp.com', port=8080)
import sentry_sdk
import os
from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://f7a65db35ea04b4fafb93135404a9465@o514688.ingest.sentry.io/5618301",
    integrations=[BottleIntegration()]
)
# Обработчик для пути '/'
@route('/')  
def index():  
    return "Hello, peoples!"

# Обработчик для пути '/success'
@route('/success')  
def success():  
    return "It is SUCCESS!"

# Обработчик для пути '/fail'
@route('/fail')  
def error():  
    raise RuntimeError("There is my error!")

# Запуск сервера
port = os.environ.get('PORT', 5000)
run(host='0.0.0.0', port=port)
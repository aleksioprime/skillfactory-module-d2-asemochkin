import sentry_sdk
import os
from bottle import route, run
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(dsn=os.environ.get("SENTRY_DSN"), integrations=[BottleIntegration()])

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
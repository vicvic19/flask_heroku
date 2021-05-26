from flask import Flask
print("Logro llegar al archivo de afuera")

app = Flask(__name__)

print("Logro llegar al archivo de afuera parte 2")
@app.route('/')

print("Logro llegar al archivo de afuera parte 3")
def hello_world():
    return('Hello World Victor de más afuera!')
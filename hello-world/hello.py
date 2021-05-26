from flask import Flask
print("Logro llegar al archivo")
app = Flask(__name__)

@app.route('/')
def hello_world():
    return('Hello World Victor!')
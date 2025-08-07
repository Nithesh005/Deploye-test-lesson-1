from time import sleep
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World! This is a Flask app."

@app.route('/hello')
def hello():
    return "Hello, I'm here .. !"

# if __name__ == '__main__':
#     app.run(debug=True, port=5001)

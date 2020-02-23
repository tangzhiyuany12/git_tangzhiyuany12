
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def hello_world1():
    return 'test1'

if __name__ == '__main__':
    app.run("0.0.0.0",port=5007,debug=True)

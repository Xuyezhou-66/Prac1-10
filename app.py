from flask import Flask

app = Flask(__name__)


@app.route('/')
def name():
    return 'XUYEZHOU 13716148'

if __name__ == '__main__':
    app.run()

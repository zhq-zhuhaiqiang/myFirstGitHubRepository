# -*- coding: utf-8 -*-
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "您好，欢迎来到 Cloud Studio ！"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
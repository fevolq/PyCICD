#!-*- coding:utf-8 -*-
# python3.7
# CreateTime: 2023/7/4 19:14
# FileName:

from flask import Flask

app = Flask(__name__)

count = 0


@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/hi/<name>')
def hi(name):
    global count
    count += 1
    return f'Hi, {name}.<br><br>Times: {count}'


if __name__ == '__main__':
    app.run(
        host='0.0.0.0'
    )

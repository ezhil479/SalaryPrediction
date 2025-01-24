# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def func1():
    return '<h1>Hello india</h1>'

@app.route('/ezhil')
def funci():
    return '<h1><b><morgue>My Name Is Ezhil</morgue></b></h1>'

if __name__ =='__main__':
    app.run(debug=True)
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 12:34:30 2022

@author: HP
"""

from flask import Flask, render_template, request
import pickle
import sklearn

app = Flask(__name__)

@app.route('/')
def fun1():
    return render_template('info.html')


@app.route('/predict', methods=['POST'])


def fun2():
    name=request.form['name']
    exp=float(request.form['exp'])
    mymodel1=pickle.load(open('model1.pkl','rb'))
    sal=mymodel1.predict([[exp]])
    return '<h1>HI {}, thank you, your predicted salary is = {}</h1>'.format(name,sal[0])


#now i want to run this app
if __name__  =='__main__':
    app.run(debug=True) 
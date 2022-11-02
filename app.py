# -*- coding: UTF-8 -*-
from flask import Flask, render_template, request, redirect, url_for
import os
import datetime as dt

app = Flask(__name__)

os_name = os.name
os_log = os.getlogin()

# For Task with for
os_information = [os_name, os_log]


@app.route('/')
def about():
    date = dt.datetime.now()
    return render_template('index.html',
                           name='Oleh Koval', user_info=request.headers.get('User-Agent'),
                           os_information=os_information, date=date)


@app.route('/education')
def education():
    date = dt.datetime.now()
    return render_template('education.html', user_info=request.headers.get('User-Agent'),
                           os_information=os_information, date=date)


@app.route('/skills')
def skills():
    date = dt.datetime.now()
    return render_template('skills.html', user_info=request.headers.get('User-Agent'),
                           os_information=os_information, date=date)


# Redirect
@app.route('/home')
def home():
    return redirect(url_for('about'))


if __name__ == '__main__':
    app.run(debug=True)

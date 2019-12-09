#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')
def accueil():
    return render_template('home.html', titre="Bienvenue !")

if __name__ == '__main__':
    app.run(debug=True)

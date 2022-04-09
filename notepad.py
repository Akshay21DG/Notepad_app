# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 10:10:38 2022

@author: sawant
"""

from flask import Flask, render_template, request
import os

app = Flask(__name__)

path=""
name=""


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/add", methods=["POST"])
def create_new():
    global path
    global name
    path = request.form.get("path")
    name = request.form.get("name")
    path=path.replace('\ooo','/ooo')
    path=path.replace('\f','/f')
    path=path.replace('\b','/b')
    path=path.replace('\t','/t')
    path=path.replace('\r','/r')
    path=path.replace('\n','/n')
    path=path.replace('\\','/')
    if not os.path.exists(path):
        os.makedirs(path)
    return render_template("notepad.html")

@app.route("/new", methods=["POST"])
def save_text():
    global path
    global name
    text=request.form.get("text")
    filename = path+'/'+name
    f=open(filename,"w+")
    f.write(text)
    f.close()
    return render_template('base.html')    


if __name__ == "__main__":
    app.run(debug=True, use_reloader = False)

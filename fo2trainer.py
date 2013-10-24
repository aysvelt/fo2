#!/usr/bin/python
import os
from flask import Flask, request, redirect, url_for, make_response
from flask import render_template
from random import randint
from savedat import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/home/ayin/tmp/"

@app.route("/")
def mainpage():
    sessionid = request.cookies.get('sessionid')
    if sessionid:
        fhpath = "/home/ayin/tmp/" + str(sessionid)
        fh = open(fhpath)
        savedat = SaveDat(fh)
        return render_template('index.html', savedat=savedat)
    else:
        return render_template('upload.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        randid = randint(1,9999999999999999999999999999999)
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(randid)))
        resp = make_response(redirect('/'))
        resp.set_cookie('sessionid', str(randid))
        return resp
    return ''

@app.route('/pop')
def pop():
    resp = make_response(redirect('/'))
    resp.set_cookie('sessionid', '', expires=0)
    return resp
 
if __name__ == "__main__":
    app.debug = True
    app.run()


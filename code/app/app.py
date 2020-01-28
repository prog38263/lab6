import os
import socket
from flask import Flask
from flask import render_template, flash

app = Flask(__name__,
        static_url_path='',
        static_folder='static',
        template_folder='templates')

@app.route('/')
def index():
    return """ 
        <a href="/simple">Simple Clickjacking Example</a><br><br>
        <a href="/maliciousad">Malicious iFrame Clickjacking Example</a>
    """

@app.route('/simple')
def simpleclickjack():
    return render_template("trivial-clickjack.html")


@app.route('/maliciousad')
def iframeexample():
    return render_template("malicious-ad.html")


from flask import Flask, Request, request, make_response, redirect, render_template, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

""" Ten en cuenta que para correr el servidor de flask, debes de crear una variable de entorno en linux cuyo valor sea el
nombre del archivo principal en flask"""

@app.route("/")
def home():
    contexto="Home"
    return render_template("index.html",context=contexto)


@app.route("/service")
def services():
    pass

@app.route("/proyects")
def proyects():
    pass

@app.route("/contactanos")
def mensajes():
    pass
from flask import render_template, url_for, redirect
from fakesite import app
from flask_login import login_required
from fakesite.forms import FormLogin, FormCriarConta


@app.route("/", methods=["GET", "POST"])

def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)
'''

@app.route("/", methods=["GET", "POST"])

def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)
    
@app.route("/criarconta")
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)

@app.route("/perfil/<usuario>")
@login_required
def perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
'''
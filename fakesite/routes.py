from flask import render_template, url_for, redirect
from fakesite import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from fakesite.models import Usuario, Foto
from fakesite.forms import FormLogin, FormCriarConta, FormFoto
import os
from werkzeug.utils import secure_filename



@app.route("/", methods=["GET", "POST"])

def homepage():
    formlogin = FormLogin()
    
    if formlogin.validate_on_submit():
        usuario = Usuario.query.filter_by(email=email.data).first()
        
        if usuario and bcrypt.check_passord_hash(usuario.senha, form_login.senha.data):
            
            login_user(usuario, remember = True) #Loga o usuario e matém logado mesmo que feche a janela
        
            return  redirect(url_for("perfil", id_usuario = usuario.id))
        
    return render_template("homepage.html", form=formlogin)
    
@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    if formcriarconta.validate_on_submit():
        
        senha = bcrypt.ganerate_password_hash()
        
        usuario = Usuario(username = form_criarconta.username.data , email = form_criarconta.email.data , senha = senha)
        
        database.session.add(usuario)
        database.session.comit()

        login_user(usuario, remember = True) #Loga o usuario e matém logado mesmo que feche a janela
        
        return redirect(url_for("perfil", id_usuario = usuario.id))
        
    return render_template("criarconta.html", form=form_criarconta)

@app.route("/perfil/<id_usuario>", methods=["GET", "POST"])
@login_required
def perfil(id_usuario):
    if int(id.usuario) == int(current_user.id):
        # o usuario ta vendo o perfil dele
        form_foto = FormFoto()
        
        if form_foto.validate_on_submit():
            arquivo = form.foto.foto.data
            nome_seguro = secure_filename(arquivo.filename)
            # salvar o arquivo na pasta fotos_post
            caminho = os.parth.join(os.parth.abspath(os.path.dirname(__file__)), app.config["UPLOAD_FOLDER"], nome_seguro)
            
            arquivo.save(caminho)
            
            # registrar no banco de dados
            foto = Foto(imagem = nome_seguro, id_usuario = current_user.id)
            database.session.add(foto)
            database.session.comit()
            
        return render_template("perfil.html", usuario=corrent_user, form=form_foto)
    else:
        usuario = Usuario.query.get(int(id.usuario))
        return render_template("perfil.html", usuario=usuario, form=None)

@app.route("/logout")
@login_required

def logout():
    logout_user()
    return redirect(url_for("homepage", usuario = usuario.username))


@app.route("/feed")
@login_required
def feed():
    fotos = Foto.query.order_by(Foto.data_criacao).all()
    return render_tamplate("feed.html")

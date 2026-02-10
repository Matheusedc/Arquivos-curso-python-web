from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db" # Configura o banco de dados da aplicação.
app.config["SECRET_KEY"] = "c6d4a322f3f58fa047363041458e407c" # Define a chave secreta da aplicação.
app.config["UPLOAD_FOLDER"] = "static/fotos_posts" # onde as fotos ficarão salvas

database = SQLAlchemy(app)
bcrypt = Bcrypt(app) # Inicializa o Bcrypt no app.
login_manager = LoginManager(app) # Inicializa o gerenciador de login.
login_manager.login_view = "homepage" # Define para onde o usuário será redirecionado se tentar acessar
# uma rota protegida sem estar logado.

from fakesite import routes
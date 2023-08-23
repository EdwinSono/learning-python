from flask import Flask
from flask import request
from flask import session
from markupsafe import escape
from Usuario import *
from UsuarioNatural import *
from UsuarioJuridico import *

app = Flask(__name__)
# global usuarios

@app.route('/')
def hello():
  return 'Hello, Práctica 4!'

@app.route('/usuario', methods=['POST'])
def crear_usuario():
  global usuarios
  request_data = request.get_json()
  usuario = Usuario(request_data['tipoUser'], request_data['usuario'], request_data['email'], request_data['password'])
  usuarioVer = usuario.ver()
  print("s", usuarioVer)
  usuarios.append(usuarioVer)
  return usuarioVer

@app.route('/usuario', methods=['GET'])
def ver_usuario():
  # usuario = Usuario('dni', 'winso','ed@fr.com', "45027257")
  print("s", usuarios)
  return f'User {escape(usuarios)}'

@app.route('/usuario/<typeUser>')
def show_post(typeUser):
  if typeUser == ruc: user = usuario.ver()
  if typeUser == dni: user = usuario.ver()
  return user
  # show the post with the given id, the id is an integer
  # return f'Post {post_id}'

@app.route('/usuario/<path:subpath>')
def show_subpath(subpath):
  # show the subpath after /path/
  return f'Subpath {escape(subpath)}'


# export FLASK_APP=src/app/server
# export FLASK_ENV=development
# flask run -p 5001

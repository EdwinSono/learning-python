import math

class Usuario():
  def __init__(self, tipoUser, usuario, email, password):
    self.usuario = usuario
    self.email = email
    self.password = password
    self.tipoUser = tipoUser

  def ver(self):
    return {
      "tipoUser": self.tipoUser,
      "usuario": self.usuario,
      "email": self.email,
      "password": self.password
    }

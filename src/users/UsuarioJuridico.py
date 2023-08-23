from Usuario import *

class UsuarioJuridico(Usuario):
  def __init__(self, type, usuario, email, password, ruc, razonSocial):
    super().__init__(type, usuario, email, password)
    self.ruc = ruc
    self.razonSocial = razonSocial

  def ver(self):
    print("----------------------")
    print("type", self.type)
    print("ruc", self.ruc)
    print("razonSocial", self.razonSocial)

from Usuario import *

class UsuarioNatural(Usuario):
  def __init__(self, typeUsuario, usuario, email, password, dni, apellidoP, apellidoM, nombres):
    super().__init__(typeUsuario, usuario, email, password)
    self.dni = dni
    self.apellidoP = apellidoP
    self.apellidoM = apellidoM
    self.nombres = nombres

  def ver(self):
    return {
      typeUsuario: self.typeUsuario,
      apellidoP: self.type,
      apellidoP: self.apellidoP,
      apellidoM: self.apellidoM,
      nombres: self.nombres
    }


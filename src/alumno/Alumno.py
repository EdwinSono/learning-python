import math

class Alumno():
  def __init__(self, nombre, nota1, nota2, nota3, nota4):
    self.nombre = nombre
    self.nota1 = nota1
    self.nota2 = nota2
    self.nota3 = nota3
    self.nota4 = nota4

  def promedio(self):
    lista = [self.nota1,self.nota2, self.nota3, self.nota4]
    lista.remove(min(lista)) 
    return round((lista[0] + lista[1] + lista[2]) / 3, 2 )

  def condicion(self):
    if self.promedio() < 8:
      condicion = 'Repite'
    elif self.promedio() >= 8 and self.promedio() < 13:
      condicion = 'Desaprobado'
    elif self.promedio() >= 13:
      condicion = 'Aprobado'
    return condicion

  def listar(self):
    print("----------------------")
    print("nombre", self.nombre)
    print("promedio", self.promedio())
    print("condicion", self.condicion())
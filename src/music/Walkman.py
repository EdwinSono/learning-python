from ReproductorMusical import *

class Walkman(ReproductorMusical):
  def __init__(self, nombre, marca, ano_fabricacion, cantidad_reparaciones, tipos_bateria):
    super().__init__(nombre, marca, ano_fabricacion, cantidad_reparaciones)
    self.tipos_bateria = tipos_bateria

  def mostrar(self):
    print("--------Walkman--------------")
    print("Tipos de batería:", self.tipos_bateria)

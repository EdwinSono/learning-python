from ReproductorMusical import *

class CDPlayer(ReproductorMusical):
  def __init__(self, nombre, marca, ano_fabricacion, cantidad_reparaciones, cantidad_cd_bandeja, material_lector_optico, cantidad_limpieza_cabezal):
    super().__init__(nombre, marca, ano_fabricacion, cantidad_reparaciones)
    self.cantidad_cd_bandeja = cantidad_cd_bandeja
    self.material_lector_optico = material_lector_optico
    self.cantidad_limpieza_cabezal = cantidad_limpieza_cabezal

  def aumentarLimpiezaCabezal(self, number):
    self.cantidad_limpieza_cabezal += number

  def mostrar(self):
    print("---------CDPlayer-------------")
    print("Cantidad cd bandeja:", self.cantidad_cd_bandeja)
    print("Material lector óptico:", self.material_lector_optico)
    print("Cantidad limpieza cabezal:", self.cantidad_limpieza_cabezal)

from ReproductorMusical import *

class Tocadisco(ReproductorMusical):
  def __init__(self, nombre, marca, ano_fabricacion, cantidad_reparaciones, cantidad_vueltas_minutos, material_aguja, cantidad_cambios_aguja):
    super().__init__(nombre, marca, ano_fabricacion, cantidad_reparaciones)
    self.cantidad_vueltas_minutos = cantidad_vueltas_minutos
    self.material_aguja = material_aguja
    self.cantidad_cambios_aguja = cantidad_cambios_aguja

  def aumentarCantidadAgujas(self, number):
    self.cantidad_cambios_aguja += number

  def mostrar(self):
    print("---------Tocadisco-------------")
    print("Cantidad vueltas minutos", self.cantidad_vueltas_minutos)
    print("Material aguja", self.material_aguja)
    print("Cantidad cambios aguja", self.cantidad_cambios_aguja)

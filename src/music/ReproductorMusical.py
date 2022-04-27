class ReproductorMusical:
  def __init__(self, nombre, marca, ano_fabricacion, cantidad_reparaciones):
    self.nombre = nombre
    self.marca = marca
    self.ano_fabricacion = ano_fabricacion
    self.cantidad_reparaciones = cantidad_reparaciones

  def aumentarCantidadReparaciones(self):
    self.cantidad_reparaciones += 1

  def mostrar(self):
    print("----------------------")
    print("Nombre:", self.nombre)
    print("Marca:", self.marca)
    print("Año de fabricacion:", self.ano_fabricacion)

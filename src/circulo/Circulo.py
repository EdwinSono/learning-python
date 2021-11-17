import math

class Circulo():
  def __init__(self, radio):
    self.radio = radio

  def circunferencia(self):
    return 2*math.pi*self.radio

  def area(self):
    return math.pi*self.radio**2

  def listar(self):
    print("----------------------")
    print("radio", self.radio)
    print("circunferencia", self.circunferencia())
    print("area", self.area())
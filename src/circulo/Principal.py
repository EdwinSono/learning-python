from Circulo import *

try:
  radio = float(input('Ingrese radio de un circulo: '))
except:
  print('Debe ingresar un valor numerico')
else:
  circulo = Circulo(radio)
  circulo.listar()

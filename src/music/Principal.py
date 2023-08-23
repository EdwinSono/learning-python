# from ReproductorMusical import *

# try:
#   print('Reproductor Musical\n')
#   nombre = input('Nombre: ').capitalize()
#   marca = input('Marca: ').capitalize()
#   ano_fabricacion = int(input('Año de fabricación: '))
#   cantidad_reparaciones = int(input('Cantidad de repaciones: '))
# except:
#   print('Debe ingresar los valores con el tipo de dato correcto')
# else:
#   reproductorMusical = ReproductorMusical(nombre, marca, ano_fabricacion, cantidad_reparaciones)
#   reproductorMusical.mostrar()
  
from Tocadisco import *
tocadisco = Tocadisco("Sony", "PS3", 2010, 3, 5, 'disco', 8)
tocadisco.aumentarCantidadAgujas(3)
tocadisco.mostrar()

from CDPlayer import *
cdPlayer = CDPlayer("Sony", "PS3", 2010, 3, 100, 'plata', 10)
cdPlayer.aumentarLimpiezaCabezal(2)
cdPlayer.mostrar()

from Walkman import *
cdPlayer = Walkman("Sony", "PS3", 2010, 3, 'pilas AAA')
cdPlayer.mostrar()

from Alumno import *

nombre = raw_input('Ingrese nombre del alumno: ').capitalize()
nota1 = int(input('Ingrese la nota 1: '))
nota2 = int(input('Ingrese la nota 2: '))
nota3 = int(input('Ingrese la nota 3: '))
nota4 = int(input('Ingrese la nota 4: '))

alumno = Alumno(nombre, nota1, nota2, nota3, nota4)
alumno.listar()

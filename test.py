# ESTE ARCHIVO ES SOLO DE PRUEBAS
# ESTOY BUSCANDO LA FORMA DE GUARDAR TODO LO INTRODUCIDO AL INPUT EN UNA LISTA SIN BORRAR NI SOBREESCRIBIR EL CONTENIDO ANTERIOR
# uno = float(input('dime un numero con decimal: '))
# dos = float(input('dime otro: '))

# print(uno - dos)
from diccionario import *

productos = input('Dime algo: ')

resultado = diccionario.get(productos, 'No esta, agregalo')
print(resultado)
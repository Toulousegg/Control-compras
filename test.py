# ESTE ARCHIVO ES SOLO DE PRUEBAS
# ESTOY BUSCANDO LA FORMA DE GUARDAR TODO LO INTRODUCIDO AL INPUT EN UNA LISTA SIN BORRAR NI SOBREESCRIBIR EL CONTENIDO ANTERIOR
# uno = float(input('dime un numero con decimal: '))
# dos = float(input('dime otro: '))

# print(uno - dos)
from distutils.log import info
from diccionario import *

productos = input('Dime algo: ')

# resultado = diccionario.has_key(productos) FAIL

# if resultado == True:
#     ID = diccionario(productos)
#     print(ID)

# else: 
#     print('Este producto no esta')

resultado = diccionario.get(productos, 'Este producto no esta')
Info = diccionario[productos]
print (Info)
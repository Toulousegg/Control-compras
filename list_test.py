# ESTE ARCHIVO ES SOLO DE PRUEBAS
# ESTOY BUSCANDO LA FORMA DE GUARDAR TODO LO INTRODUCIDO AL INPUT EN UNA LISTA SIN BORRAR NI SOBREESCRIBIR EL CONTENIDO ANTERIOR

i = 0
lista = list()


def agregar_contenido():
    i=+1
    numero = int(input('Dime un número: '))
    lista.append(numero)

    if i == 5:
        print(lista)

while i <= 5:
    agregar_contenido()
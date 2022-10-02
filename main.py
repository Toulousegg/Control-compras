import datetime
from diccionario import *
from typing import Any, Hashable, Iterable, Optional

a = input('¿Vas de compras?: ')
d = datetime.datetime.now().strftime('%d-%m_%H-%M')
i = 0
x = 1
caracter_separador = '*'
lista_de_precios = list()

if a == 'si':
    txt = open(f'Compras del {format(d)}.txt', 'w')
    txt.write('Producto            Precio            Numero de productos comprados\n\n')

    while a == 'si':
        i+=1
        total = sum(lista_de_precios) #la función 'sum()' suma los elementos de una lista o tupla de una forma sencilla y rápida
        productos = input('Dime el producto: ')

        # guardar los productos en un diccionario, y si ya estan solo obtener si ID        
        if productos in diccionario == True:
            
            def buscar_dicc(it: Iterable[dict], clave: Hashable, valor: Any) -> Optional[dict]:
                for dicc in it:
                    if dicc[clave] == valor:
                        return dicc

                    else:
                        diccionario.append(productos)
 


        if productos == 'Medidor':
            from medidor_kg import *
            PesoGR
            Precio_de_peso
            Producto
            lista_de_precios.append(PrecioKG)
            txt.write(f'{Producto}               ')
            txt.write(f'{Precio_de_peso}/{PesoGR}Gr.                 ')
            txt.write(f'{PrecioKG}                \n')
        
        if productos == 'termine':
            txt.write('---------------------------------------------------------\n')
            txt.write('                    TOTAL\n')
            txt.write(f'                      {total}')
            txt.close()
            break
        
        print(f'{total}')

        precios = float(input('Dime el precio del producto: '))
        
        cantidad = int(input('¿Cuantos articulos vas a llevar?:'))

        #if cantidad == int:
        cantidad_total = cantidad*precios

        lista_de_precios.append(cantidad_total)
        txt.write(f'{productos}               ')

        if cantidad >= 2:
            txt.write(f'{precios}$ X {cantidad}            ')

        else:
            txt.write(f'{cantidad_total}$               ')

        txt.write(f'Articulo numero {i}\n')

if a == 'no':
    print('Ok.')
    quit()
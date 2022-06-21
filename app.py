import datetime


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
        productos = input('Dime el producto: ')
        
        if productos == 'termine':
            total = sum(lista_de_precios) #la función 'sum()' suma los elementos de una lista o tupla de una forma sencilla y rápida
            txt.write('---------------------------------------------------------\n')
            txt.write('                    TOTAL\n')
            txt.write(f'                      {total}')
            txt.close()
            break
        
        precios = float(input('Dime el precio del producto: '))
        
        cantidad = int(input('¿Cuantos articulos vas a llevar?:'))

        #if cantidad == int:
        cantidad_total = cantidad*precios

        #if caracter_separador in precios:
            #separado = precios.split(caracter_separador)
            #n1 = lambda separado, x: [separado[i:i+x] for i in range(0, len(separado), x)] #separador de elementos dentro de listas
            #output = n1(separado, x) #acá separé los elementos pero aún no están guardados en ninguna variable diferente para poder hacer la multiplicación
            ##tengo que guardar los dos números en variables separadas para multiplicarlas
            #lista_de_precios.append(output)
            #continue
            #la idea es separar los dos números y ponerlos en variables diferentes para después multiplicarlos y poner el total de la multiplicación en la lista de suma

        lista_de_precios.append(cantidad_total)
        txt.write(f'{productos}               ')

        if cantidad >= 2:
            txt.write(f'{precios}$ X {cantidad}            ')

        else:
            txt.write(f'{cantidad_total}$               ')

        txt.write(f'Articulo numero {i}\n')

if a == 'no':
    print('¿Tons para que me abres?, bruja.')
    quit()
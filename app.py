import datetime


a = input('¿Vas de compras?: ')
b = a
d = datetime.datetime.now().strftime('%d-%m_%H-%M')
i = 0

if a == 'si':
    txt = open(f'Compras del {format(d)}', 'w')

    for answer in b:
        i+=1
        productos = input('Dime el producto: ')
        precio = float(input('Dime el precio del producto: ')) #error a la hora de transforma a float, no se que ocurre...
        lista_de_precios = list(precio)#esto deberia guardar todos los valores puestos en precio para depués sumarlos, aún no se como hacerlo
        txt.write(f'{productos}...............') #no obtiene más de un argumento y yo necesito escribir 3 en el .txt, tratare de cambiar de metodo.
        txt.write(f'{precio}...............')
        txt.write(f'Articulo número {i}\n')

        if productos == 'Termine' 'termine':
            txt.close()
            
            break

if a == 'no':
    print('¿Tons para que me abres?, bruja.')
    quit()

else:
    print('Que')
import datetime


a = input('¿Vas de compras?: ')
d = datetime.datetime.now().strftime('%d-%m_%H-%M')
i = 0

if a == 'si':
    txt = open(f'Compras del {format(d)}.txt', 'w')
    txt.write('Producto            Precio            Numero de productos comprados\n\n')

    while a == 'si':
        i+=1
        productos = input('Dime el producto: ')
        if productos == 'termine':
            txt.close()
            #suma de todos los valores escritos en precio para dar un total y printiarlo
            break
        
        precio = int(input('Dime el precio del producto: ')) #error a la hora de transforma a float, no se que ocurre...
        lista_de_precios = [precio]#esto deberia guardar todos los valores puestos en precio para después sumarlos, aún no se como hacerlo
        txt.write(f'{productos}               ')
        txt.write(f'{precio}$               ')
        txt.write(f'Articulo numero {i}\n')

if a == 'no':
    print('¿Tons para que me abres?, bruja.')
    quit()

#else:
    #print('Que so rra')
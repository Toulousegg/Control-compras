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
        precio = int(input('Dime el precio del producto: '))
        txt.write(productos, precio, i)
        
        if productos == 'Termine' 'termine':
            txt.close()
            break

if a == 'no':
    print('¿Tons para que me abres?, bruja.')
    quit()

else:
    print('Que')
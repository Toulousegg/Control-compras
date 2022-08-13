producto = input('¿Qué producto es?: ')
precio1k = float(input(f'Dime el precio de un Kg de {producto}: '))
precioplusk = float(input(f'Dime el precio del paquete de {producto} que pesa más: '))
diferencia = None
#k = int(input(f'¿Cuantos Kg de diferencia hay?: '))
#para no haga tantas preguntas puedo hacer un bucle 
# para reste el valor de 1 kg al de mayor peso hasta que 
# no se pueda restar más (de negativo), y sacar la diferencia,
# la idea es que nos diga cual de los dos nos combiene más
# y cuanto nos ahorramos. #

def beneficios():
#     mult = k*precio1k
#     if mult >= precioPlusk:
#         print(f'te sale mejor comprar los {k} Kg más')
    
#     if mult <= precioPlusk:
#         print(f'No vale la pena comprar más peso')

#     if mult == precioPlusk:
#         print('Es la misma vaina')
    for diferencia in diferencia:

        if precioplusk >= precio1k:
            resta = precioplusk - precio1k
        
        if precioplusk <= precio1k:
            print(diferencia)
            quit()

beneficios()
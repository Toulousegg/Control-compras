producto = input('¿Qué producto es?: ')
precio1k = int(input(f'Dime el precio de un Kg de {producto}: '))
precioPlusk = int(input(f'Dime el precio del paquete de {producto} que pesa más: '))
K = int(input(f'¿Cuantos Kg de diferencia hay?: '))
#para no haga tantas preguntas puedo hacer un bucle 
# para reste el valor de 1 kg al de mayor peso hasta que 
# no se pueda restar más (de negativo), y sacar la diferencia,
# la idea es que nos diga cual de los dos nos combiene más
# y cuanto nos ahorramos. #

def beneficios():
    while precioPlusk >= precio1k:
        resta = precioPlusk - precio1k
        if precioPlusk <= precio1k:
            diferencia = resta
            print(diferencia)

beneficios()
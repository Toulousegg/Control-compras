from tkinter import *

ventana = Tk()
ventana.title('Calculadora')

#entrada
e_texto = Entry(ventana, font= ('Calibri, 20'))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 50, pady = 5)

#botones
boton1 = Button(ventana, text = '1', width = 5, height = 2)
boton2 = Button(ventana, text = '2', width = 5, height = 2)
boton3 = Button(ventana, text = '3', width = 5, height = 2)
boton4 = Button(ventana, text = '4', width = 5, height = 2)
boton5 = Button(ventana, text = '5', width = 5, height = 2)
boton6 = Button(ventana, text = '6', width = 5, height = 2)
boton7 = Button(ventana, text = '7', width = 5, height = 2)
boton8 = Button(ventana, text = '8', width = 5, height = 2)
boton9 = Button(ventana, text = '9', width = 5, height = 2)
boton0 = Button(ventana, text = '0', width = 15, height = 2)

BotonSum = Button(ventana, text = '+', width = 5, height = 2)
BotonResta = Button(ventana, text = '-', width = 5, height = 2)
BotonMulti = Button(ventana, text = '*', width = 5, height = 2)
BotonDiv = Button(ventana, text = '/', width = 5, height = 2)

BotonParentesisAbriendo = Button(ventana, text = '(', width = 5, height = 2)
BotonParentesisCerrando = Button(ventana, text = ')', width = 5, height = 2)
BotonPunto = Button(ventana, text = '.', width = 5, height = 2)
BotonIgual = Button(ventana, text = '=', width = 5, height = 2)
BotonBorrado = Button(ventana, text = 'C', width = 5, height = 2) #borra el ultimo digito
BotonLimpiar = Button(ventana, text = 'AC', width = 5, height = 2) #borra todo

#posicionamiento

boton1.grid(row = , column = , padx = 5, pady = 5)
boton2.grid(row = , column = , padx = 5, pady = 5)
boton3.grid(row = , column = , padx = 5, pady = 5)
boton4.grid(row = , column = , padx = 5, pady = 5)
boton5.grid(row = , column = , padx = 5, pady = 5)
boton6.grid(row = , column = , padx = 5, pady = 5)
boton7.grid(row = , column = , padx = 5, pady = 5)
boton8.grid(row = , column = , padx = 5, pady = 5)
boton9.grid(row = , column = , padx = 5, pady = 5)
boton0.grid(row = , column = , padx = 5, pady = 5)

BotonSum.grid(row = 4, column = 4, padx = 5, pady = 5)
BotonResta.grid(row = 3, column = 4, padx = 5, pady = 5)
BotonMulti.grid(row = 2, column = 3, padx = 5, pady = 5)
BotonDiv.grid(row = 2, column = 2, padx = 5, pady = 5)
BotonParentesisAbriendo.grid(row = 1, column = 1, padx = 5, pady = 5)
BotonParentesisCerrando.grid(row = 1, column = 2, padx = 5, pady = 5)
BotonPunto.grid(row = 6, column = 3, padx = 5, pady = 5)
BotonIgual.grid(row = 6, column = 4, padx = 5, pady = 5)
BotonBorrado.grid(row = 2, column = 4, padx = 5, pady = 5)
BotonLimpiar.grid(row = 1, column = 3, padx = 5, pady = 5)

ventana.mainloop()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

import datetime


class ComprasApp(App):

    def build(self):

        self.total = 0
        self.productos_guardados = []

        # ---------- CONTENEDOR PRINCIPAL ----------
        principal = BoxLayout(
            orientation='vertical',
            padding=15,
            spacing=10
        )

        # ---------- TITULO ----------
        titulo = Label(
            text='LISTA DE COMPRAS',
            size_hint=(1, 0.12),
            font_size=30
        )

        # ---------- INPUTS ----------
        self.producto = TextInput(
            hint_text='Producto',
            multiline=False,
            size_hint=(1, 0.1)
        )

        self.precio = TextInput(
            hint_text='Precio',
            multiline=False,
            input_filter='float',
            size_hint=(1, 0.1)
        )

        self.cantidad = TextInput(
            hint_text='Cantidad',
            multiline=False,
            input_filter='int',
            size_hint=(1, 0.1)
        )

        # ---------- BOTON AGREGAR ----------
        boton_agregar = Button(
            text='Agregar Producto',
            size_hint=(1, 0.12)
        )

        boton_agregar.bind(on_press=self.agregar)

        # ---------- BOTON TERMINAR ----------
        boton_terminar = Button(
            text='Terminar Compra',
            size_hint=(1, 0.12)
        )

        boton_terminar.bind(on_press=self.terminar)

        # ---------- TOTAL ----------
        self.total_label = Label(
            text='TOTAL: $0',
            size_hint=(1, 0.1),
            font_size=24
        )

        # ---------- SCROLL ----------
        scroll = ScrollView()

        self.lista = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None
        )

        self.lista.bind(minimum_height=self.lista.setter('height'))

        scroll.add_widget(self.lista)

        # ---------- AGREGAR WIDGETS ----------
        principal.add_widget(titulo)
        principal.add_widget(self.producto)
        principal.add_widget(self.precio)
        principal.add_widget(self.cantidad)
        principal.add_widget(boton_agregar)
        principal.add_widget(boton_terminar)
        principal.add_widget(scroll)
        principal.add_widget(self.total_label)

        return principal

    # ---------- FUNCION AGREGAR ----------
    def agregar(self, instance):

        producto = self.producto.text.strip()
        precio = self.precio.text.strip()
        cantidad = self.cantidad.text.strip()

        if producto == '' or precio == '' or cantidad == '':
            return

        precio = float(precio)
        cantidad = int(cantidad)

        subtotal = precio * cantidad

        self.total += subtotal

        # GUARDAR DATOS
        self.productos_guardados.append({
            'producto': producto,
            'precio': precio,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

        item = Label(
            text=f'{producto} | {cantidad} x ${precio} = ${subtotal:.2f}',
            size_hint_y=None,
            height=40
        )

        self.lista.add_widget(item)

        self.total_label.text = f'TOTAL: ${self.total:.2f}'

        # limpiar campos
        self.producto.text = ''
        self.precio.text = ''
        self.cantidad.text = ''

    # ---------- FUNCION TERMINAR ----------
    def terminar(self, instance):

        fecha = datetime.datetime.now().strftime('%d-%m-%y_%H-%M')

        nombre_archivo = f'Compras_{fecha}.txt'

        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:

            # TITULO
            archivo.write(f'{"Producto":<25}')
            archivo.write(f'{"Precio":<20}')
            archivo.write(f'{"Cantidad":<15}\n')

            archivo.write('-' * 60 + '\n')

            # PRODUCTOS
            for i, item in enumerate(self.productos_guardados, start=1):

                producto = item['producto']
                precio = item['precio']
                cantidad = item['cantidad']

                archivo.write(
                    f'{producto:<25}'
                    f'${precio:.2f} x {cantidad:<12}'
                    f'Articulo numero {i}\n'
                )

            archivo.write('-' * 60 + '\n')

            # TOTAL
            archivo.write(f'\n{"TOTAL":>35}  ${self.total:.2f}')

        self.total_label.text = 'Compra guardada 🩷'


# ---------- EJECUTAR APP ----------
ComprasApp().run()
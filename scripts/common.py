import tkinter as tk
from tkinter import *
from tkinter import ttk, filedialog
import tkinter.font as font
import customtkinter

grey_1 = "#1F1F1F"
grey_2 = "#252525"
grey_3 = "#181818"
blue = "#056DCF"


def not_implemented(root):
    class Window:
        def __init__(self, parent):
            self.parent = parent
            self.parent.iconify()  # Oculta la ventana principal
            # Crear una nueva ventana para el enlace de descarga
            self.top = customtkinter.CTkToplevel()
            self.top.title('Función no implementada')

            # Establecer tamaño mínimo de la ventana
            self.top.minsize(500, 50)

            # Calcula las coordenadas para centrar la ventana
            self.screen_width = self.top.winfo_screenwidth()
            self.screen_height = self.top.winfo_screenheight()
            self.x = (self.screen_width / 2) - (500 / 2)
            self.y = (self.screen_height / 2) - (50 / 2)

            # Establece la posición de la ventana para que aparezca centrada
            self.top.geometry("+%d+%d" % (self.x, self.y))

            # Crear los widgets para el input de la URL
            message = customtkinter.CTkLabel(self.top, text='Esta función no ha sido implementada', text_color='#fff',
                                             fg_color='transparent')
            message.pack(pady=10)

            # Registrar el método on_closing como la función de devolución de llamada
            # para el evento de cierre de la ventana
            self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

        def on_closing(self):
            # Mostrar de nuevo la ventana principal
            self.parent.deiconify()

            # Cerrar la ventana de opciones
            self.top.destroy()

    Window(root)

import subprocess
import os
import sys
import platform
import ctypes
import threading
from . import common_content as common

# lista de módulos que se necesitan instalar
required_modules = ["pytube", "gofile", "pyperclip", "re", "customtkinter"]

# recorre la lista de módulos y los instala utilizando pip
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"instalando {module}")
        if module == "tkinter":
            module = "tk"
        if platform.system() == "Windows":
            subprocess.run(["pip", "install", module], capture_output=False, stdout=subprocess.PIPE, universal_newlines=True, shell=True)
        elif platform.system() == "Linux":
            subprocess.run(["pip3", "install", module], capture_output=False, stdout=subprocess.PIPE, universal_newlines=True)
        # subprocess.run(["pip", "install", module], capture_output=False, shell=True)

requirements = True
# verificar la existencia de tkinter, filedialog, tk.font, subprocess y threading
try:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk, filedialog
    import tkinter.font as font
    from tkinter import simpledialog
    import pytube
    import gofile as go
    import pyperclip
    import re
    import customtkinter

except ImportError:
    requirements = False

if not requirements:
    os.system('echo Error: tkinter, subprocess, threading, moviepy, pdf2docx, aspose.words,'
              'Pillow, ctypes, pytube, pathlib is not installed && pause >nul')
    sys.exit()


customtkinter.set_appearance_mode("dark")


def update_label(output, root):
    global label
    label = customtkinter.CTkLabel(root, text=output, width=100)
    label.configure(text_color="#fff", fg_color="transparent")
    label.grid(padx=10, pady=10, row=7, column=0, columnspan=2, sticky="nsew")


def descargar_video_youtube(root):
    global output
    global label
    class OptionsWindow:
        def __init__(self, parent):
            self.parent = parent
            self.parent.iconify()  # Oculta la ventana principal

            # Crear una nueva ventana para las opciones
            self.top = customtkinter.CTkToplevel()
            self.top.title('Opciones')

            # Establecer tamaño mínimo de la ventana
            self.top.minsize(500, 400)

            # Calcula las coordenadas para centrar la ventana
            self.screen_width = self.top.winfo_screenwidth()
            self.screen_height = self.top.winfo_screenheight()
            self.x = (self.screen_width / 2) - (500 / 2)
            self.y = (self.screen_height / 2) - (400 / 2)

            # Establece la posición de la ventana para que aparezca centrada
            self.top.geometry("+%d+%d" % (self.x, self.y))

            # Crear los widgets para el input de la URL
            url_label = customtkinter.CTkLabel(self.top, text='Introduce la URL del vídeo:') #, bg='#171515', fg='#fff')
            url_label.pack(pady=20)
            self.url_entry = customtkinter.CTkEntry(self.top) #, bg='#171515', fg='#fff')
            self.url_entry.pack(pady=20)

            # Crear los widgets para los radiobuttons
            format_label = customtkinter.CTkLabel(self.top, text='Selecciona el formato de salida:') #, bg='#171515', fg='#fff')
            format_label.pack(pady=20)

            self.format_var = StringVar()
            self.format_var.set('gif')  # Valor por defecto

            op_video = customtkinter.CTkRadioButton(self.top, text='Video', variable=self.format_var, value='video')
            op_audio = customtkinter.CTkRadioButton(self.top, text='Audio', variable=self.format_var, value='audio')

            op_video.pack()
            op_audio.pack()

            # Crear el botón para ejecutar la conversión
            convertir_button = customtkinter.CTkButton(self.top, text='Descargar', command=self.convertir) #, bg='#121111', fg='#fff')
            convertir_button.pack(pady=20)

            # Registrar el método on_closing para que se llame cuando la ventana sea cerrada
            self.top.protocol("WM_DELETE_WINDOW", self.on_closing)

        def on_closing(self):
            # Mostrar de nuevo la ventana principal
            self.parent.deiconify()

            # Cerrar la ventana de opciones
            self.top.destroy()

        def convertir(self):
            # Obtener el valor del input de la URL y del radiobutton seleccionado
            url = self.url_entry.get()
            format_file = self.format_var.get()

            # Llamar a la función de conversión con los parámetros
            if url != "":
                print(f'Convirtiendo {url} a formato {format_file}...')
                descargar(url, format_file)

                # Cerrar la ventana de opciones
                self.top.destroy()

                # Mostrar de nuevo la ventana principal
                self.parent.deiconify()

    def descargar(url, format_file):
        global output
        global label
        dest_folder = filedialog.askdirectory(
            initialdir="C:\\",
            title="Selecciona el destino del archivo"
        )
        if format_file == "video":
            video_instance = pytube.YouTube(url).streams.get_highest_resolution()
            name = video_instance.title.replace('/', '-').replace('\\', '-')\
                       .replace(':', '-').replace('*', '-').replace('?', '-') \
                       .replace('"', '').replace('<', '').replace('>', '').replace('|', '').replace(' ', '-') \
                       .replace('\'', '') + ".mp4"
            video_instance.download(filename=name, output_path=dest_folder)
        if format_file == "audio":
            video_instance = pytube.YouTube(url).streams.filter(only_audio=True).first()
            name = video_instance.title.replace('/', '-').replace('\\', '-')\
                .replace(':', '-').replace('*', '-').replace('?', '-')\
                .replace('"', '').replace('<', '').replace('>', '').replace('|', '').replace(' ', '-')\
                .replace('\'', '').replace(",", "") + ".mp3"
            video_instance.download(filename=name, output_path=dest_folder)
        print(f'Descargado {name} en {dest_folder}')
        output = str(f'Descargado {name} en {dest_folder}')
        update_label(output, root)
    OptionsWindow(root)


def compartir_archivo(root):

    class OptionsWindow:
        def __init__(self, parent):
            self.parent = parent
            self.parent.iconify()  # Oculta la ventana principal

            # Pedir el archivo a compartir
            file = filedialog.askopenfilename(initialdir="C:\\", title="Elige el archivo",
                                              filetypes=(("Todos los archivos", "*.*"),))
            if not file:  # Verificar si no se ha seleccionado ningún archivo
                # Mostrar de nuevo la ventana principal y salir
                self.parent.deiconify()
                return
            url = store_files(file)
            # Crear una nueva ventana para el enlace de descarga
            self.top = customtkinter.CTkToplevel()
            self.top.title('Enlace de descarga')

            # Establecer tamaño mínimo de la ventana
            self.top.minsize(500, 150)

            # Calcula las coordenadas para centrar la ventana
            self.screen_width = self.top.winfo_screenwidth()
            self.screen_height = self.top.winfo_screenheight()
            self.x = (self.screen_width / 2) - (500 / 2)
            self.y = (self.screen_height / 2) - (150 / 2)

            # Establece la posición de la ventana para que aparezca centrada
            self.top.geometry("+%d+%d" % (self.x, self.y))

            # Crear el widget que muestra la url generada
            url_label = customtkinter.CTkLabel(self.top, text="El enlace para compartir es: " + url["downloadPage"],
                              text_color='#fff', fg_color='transparent')
            url_label.pack(pady=10)

            # Crear el botón para Copiar
            copiar_button = customtkinter.CTkButton(self.top, text='Copiar enlace',
                                                    command=self.copiar_enlace(url_label),
                                                    fg_color="#181818", hover_color="#056DCF")
            copiar_button.pack(pady=10)

            # Crear el botón para Aceptar
            aceptar_button = customtkinter.CTkButton(self.top, text='Aceptar', command=self.on_closing,
                                                     fg_color="#181818", hover_color="#056DCF")
            aceptar_button.pack(pady=10)

        def on_closing(self):
            # Cerrar la ventana de opciones
            self.top.destroy()

            # Mostrar de nuevo la ventana principal
            self.parent.deiconify()

        def copiar_enlace(self, url_label):
            url_label_text = url_label.cget("text")
            url_match = re.search(r"http\S+", url_label_text)
            if url_match:
                url = url_match.group(0)
                self.top.clipboard_clear()
                self.top.clipboard_append(url)
    OptionsWindow(root)


def store_files(file):
    cur_server = go.getServer()
    url = go.uploadFile(file)
    return url


def traducir_texto(root):
    common.not_implemented(root)


def descargar_video_twitter(root):
    common.not_implemented(root)
import subprocess
import os
import sys
import platform

# Ruta del directorio "multitool"
multitool_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'multitool'))
sys.path.append(multitool_path)

from scripts import video_functions
from scripts import audio_functions
from scripts import image_functions
from scripts import document_functions
from scripts import other_functions
from scripts import common_content as common

# Lista de módulos que se necesitan instalar
required_modules = ["tkinter", "subprocess", "threading", "pathlib", "ctypes", "customtkinter"]
# Recorre la lista de módulos y los instala utilizando pip
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

# Verificar la existencia de tkinter, filedialog, tk.font y threading
requirements = True
try:
    import tkinter as tk
    from tkinter import *
    from tkinter import ttk, filedialog
    import tkinter.font as font
    import threading
    import pathlib
    import ctypes as ct
    import customtkinter
except ImportError:
    requirements = False

if not requirements:
    os.system('echo Error: tkinter or threading is not installed && pause >nul')
    sys.exit()

output = ""


# Solo compatible con Windows 11
def dark_title_bar():
    global root
    """
    MORE INFO:
    https://learn.microsoft.com/en-us/windows/win32/api/dwmapi/ne-dwmapi-dwmwindowattribute
    """
    root.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(root.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value),
                         ct.sizeof(value))


# Definir la ventana
root = customtkinter.CTk()
root.title("Multi-Herramienta")
root.configure(fg_color=common.grey_1)
# Establecer tamaño mínimo de la ventana
root.minsize(1280, 720)

# Calcula las coordenadas para centrar la ventana
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (1280 / 2)
y = (screen_height / 2) - (720 / 2)

# Establece la posición de la ventana para que aparezca centrada
root.geometry("+%d+%d" % (x, y))
# Establecer la barra de título oscura y maximizar la ventana si se está utilizando windows
if platform.system() == "Windows":
    dark_title_bar()
    root.state('zoomed')

# Fuente de Texto principal
main_font = customtkinter.CTkFont(family='Helvetica', size=24, weight="bold")


# Definir la clase para los botones, esta definirá su estilo y posición
class MyButton:
    def __init__(self, frame, text, command, row, column):
        self.width = 350
        self.height = 50
        self.padx = 10
        button_font = customtkinter.CTkFont(family='Helvetica', size=12, weight="bold")
        self.button = customtkinter.CTkButton(frame, command=command, width=self.width, height=self.height,
                             text=text, font=button_font, cursor="hand2", fg_color=common.grey_3, hover_color=common.blue)
        self.row = row
        self.column = column
        self.button.grid(row=row, column=column, padx=self.padx, pady=5, sticky="nsew")


# Definir el grid
#for i in range(8):
#    root.grid_rowconfigure(i, weight=1)
root.grid_rowconfigure(1, weight=1)
for i in range(1):
    root.grid_columnconfigure(i, weight=1)

# Titulo
txt = customtkinter.CTkLabel(master=root, text='Multi-Herramienta')
txt.configure(fg_color="transparent", text_color='white', pady=10, font=main_font)
txt.grid(column=0, columnspan=7, row=0, sticky="nsew")

# Texto donde se muestran los outputs de las funciones
label = customtkinter.CTkLabel(root, text=output, width=100)
label.configure(text_color="#fff", fg_color="transparent")
label.grid(padx=10, pady=10, row=7, column=0, columnspan=2, sticky="nsew")

# Crear vista de pestañas
tabview = customtkinter.CTkTabview(root)
tabview.configure(fg_color=common.grey_2)
tabview.grid(row=1, rowspan=6, column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

tabview.add("Vídeo")
tabview.add("Audio")
tabview.add("Imagen")
tabview.add("Documentos")
tabview.add("Otros")
# Establecer pestaña por defecto
tabview.set("Vídeo")

# Agregar botones a la pestaña de vídeo
convertir_mp4_a_gif = MyButton(tabview.tab("Vídeo"), text='Convertir archivos MP4 a GIF',
                               command=lambda: video_functions.mp4_to_gif(root), column=0, row=1)


# Agregar botones a la pestaña de imagenes
convertir_png_a_jpg = MyButton(tabview.tab("Imagen"), text='Convertir archivos PNG a JPG',
                               command=lambda: image_functions.png_to_jpg(output, root), column=0, row=1)
comprimir_imagen = MyButton(tabview.tab("Imagen"), text='Comprimir imágenes',
                            command=lambda: image_functions.comprimir_imagen(output, root), column=0, row=2)
# eliminar_fondo_imagen = MyButton(imagenes_tab, text='Eliminar fondo de una imágen',
#                                     command=lambda: eliminar_fondo_imagen, column=0, row=6)


# Agregar botones a la pestaña de documentos
convertir_pdf_a_docx = MyButton(tabview.tab("Documentos"), text='Convertir PDF a DOCX',
                                command=lambda: document_functions.pdf_to_docx(root), column=0, row=0)
convertir_pdf_a_epub = MyButton(tabview.tab("Documentos"), text='Convertir archivos PDF a EPUB',
                                command=lambda: document_functions.pdf_to_epub(root), column=0, row=1)
desbloquear_pdf = MyButton(tabview.tab("Documentos"), text='Desbloquear_PDF',
                                command=lambda: document_functions.desbloquear_pdf(root), column=0, row=2)
comprimir_pdf = MyButton(tabview.tab("Documentos"), text='Comprimir_PDF',
                                command=lambda: document_functions.comprimir_pdf(root), column=0, row=3)
pdf_a_powerpoint = MyButton(tabview.tab("Documentos"), text='Convertir PDF a PowerPoint',
                                command=lambda: document_functions.pdf_a_powerpoint(root), column=0, row=4)
epub_a_pdf = MyButton(tabview.tab("Documentos"), text='Convertir archivos EPUB a PDF',
                                command=lambda: document_functions.epub_a_pdf(root), column=0, row=5)
pdf_a_mobi = MyButton(tabview.tab("Documentos"), text='Convertir archivos PDF a MOBI',
                                command=lambda: document_functions.pdf_a_mobi(root), column=0, row=6)
pdf_a_texto = MyButton(tabview.tab("Documentos"), text='Convertir archivos PDF a texto plano (.txt)',
                                command=lambda: document_functions.pdf_a_texto(root), column=0, row=7)
epub_a_mobi = MyButton(tabview.tab("Documentos"), text='Convertir archivos EPUB a MOBI',
                                command=lambda: document_functions.epub_a_mobi(root), column=1, row=0)
mobi_a_epub = MyButton(tabview.tab("Documentos"), text='Convertir archivos MOBI a EPUB',
                                command=lambda: document_functions.mobi_a_epub(root), column=1, row=1)


# Agregar botones a la pestaña de otros
descargar_video_youtube = MyButton(tabview.tab("Otros"), text='Descargar video de Youtube',
                                   command=lambda: other_functions.descargar_video_youtube(root), column=0, row=1)
compartir_archivo = MyButton(tabview.tab("Otros"), text='Compartir un archivo',
                                   command=lambda: other_functions.compartir_archivo(root), column=0, row=2)
traducir_texto = MyButton(tabview.tab("Otros"), text='Traducir texto',
                                   command=lambda: other_functions.traducir_texto(root), column=0, row=3)
descargar_video_twitter = MyButton(tabview.tab("Otros"), text='Descargar video de Twitter',
                                   command=lambda: other_functions.descargar_video_twitter(root), column=0, row=4)


# Control de versión
version_label = customtkinter.CTkLabel(master=root, text="Multi-Herramienta vPre 0.3 - 16/4/2023",
                                       font=main_font, text_color="#fff", fg_color="transparent")
version_label.grid(row=8, column=1, sticky="se", padx=10, pady=10)
root.mainloop()

import subprocess
import os
import sys
import platform
from multitool.scripts import common

# lista de módulos que se necesitan instalar
required_modules = ["moviepy"]


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
    import PIL
    from PIL import Image, ImageDraw
except ImportError:
    requirements = False

if not requirements:
    os.system('echo Error: PIL or TKinter is not installed && pause >nul')
    sys.exit()


def update_label(output, root):
    global label
    label = Label(root, text=output, width=100)
    label.config(bg="#121111", fg='white')
    label.grid(padx=10, pady=10, row=7, column=0, columnspan=4, sticky="nsew")


# Convertir imagen PNG a JPG
def png_to_jpg(output, root):
    filepaths = filedialog.askopenfilenames(initialdir="C:\\", title="Elige el archivo",
                                            filetypes=(("Imágenes", "*.png"), ("all files", "*.*")))
    if len(filepaths) == 0:
        print("No files selected")
        return

    dest_folder = filedialog.askdirectory(
        initialdir="C:\\",
        title="Selecciona el destino del archivo"
    )

    for filepath in filepaths:
        print(filepath)
        output = str(filepath)

        filename = filepath.split("/")[-1]  # Get the filename from the path
        dest_filepath = f"{dest_folder}/{filename.replace('.PNG', '.jpg')}"

        png = PIL.Image.open(filepath)
        rgb_im = png.convert('RGB')
        rgb_im.save(dest_filepath)

        print(f"{filepath} saved as {dest_filepath}")
        output = str(f"{filepath} saved as {dest_filepath}")
        update_label(output, root)


# Comprimir imágenes
def comprimir_imagen(output, root):
    filepaths = filedialog.askopenfilenames(initialdir="C:\\", title="Elige el archivo",
                                            filetypes=(("Imágenes", "*.png *.jpg"), ("Todos los archivos", "*.*")))
    if len(filepaths) == 0:
        print("No files selected")
        return
    dest_folder = filedialog.askdirectory(
        initialdir="C:\\",
        title="Selecciona el destino del archivo"
    )
    for filepath in filepaths:
        print(filepath)
        output = str(filepath)
        filename = filepath.split("/")[-1]  # Get the filename from the path
        input_file = PIL.Image.open(filepath)
        output_file = dest_folder + "/" + filename
        output = Image.open(filepath)
        output.save(output_file, optimize=True, quality=80)
        print(f"{filepath} saved as {output_file}")
        output = str(f"{filepath} saved as {output_file}")
        update_label(output, root)

# Funcion desactivada por problemas de compatibilidad
# def eliminar_fondo_imagen():
#     global output
#     global label
#     filepaths = filedialog.askopenfilenames(initialdir="C:\\", title="Elige el archivo",
#                                             filetypes=(("Imágenes", "*.png *.jpg"), ("Todos los archivos", "*.*")))
#     if len(filepaths) == 0:
#         print("No files selected")
#         return
#     dest_folder = filedialog.askdirectory(
#         initialdir="C:\\",
#         title="Selecciona el destino del archivo"
#     )
#     for filepath in filepaths:
#         print(filepath)
#         output = str(filepath)
#         filename = filepath.split("/")[-1]  # Get the filename from the path
#         input_file = PIL.Image.open(filepath)
#         output_file = dest_folder + "/" + filename.replace('.jpg', '.png')
#         output = remove(input_file)
#         output.save(output_file, format='PNG')
#         print(f"{filepath} saved as {output_file}")
#         output = str(f"{filepath} saved as {output_file}")
#         update_label(output, root)

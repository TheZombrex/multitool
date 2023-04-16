import subprocess
import os
import sys
import platform
import ctypes
import threading
from . import common_content as common


# lista de módulos que se necesitan instalar
required_modules = ["pdf2docx", "aspose.words", "ctypes"]

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
    import ctypes as ct
    import aspose.words as aw
    from pdf2docx import Converter
    from tkinter import simpledialog

except ImportError:
    requirements = False

if not requirements:
    os.system('echo Error: tkinter, subprocess, threading, moviepy, pdf2docx, aspose.words,'
              'Pillow, ctypes, pytube, pathlib is not installed && pause >nul')
    sys.exit()


def update_label(output, root):
    global label
    label = Label(root, text=output, width=100)
    label.config(bg="#121111", fg='white')
    label.grid(padx=10, pady=10, row=7, column=0, columnspan=4, sticky="nsew")


def pdf_to_docx(root):
    global output
    global label
    filepaths = filedialog.askopenfilenames(initialdir="C:\\", title="Elige el archivo",
                                            filetypes=(("Documentos", "*.pdf"), ("all files", "*.*")))
    if len(filepaths) == 0:
        print("No files selected")
        return

    dest_folder = filedialog.askdirectory(
        initialdir="C:\\",
        title="Selecciona el destino del archivo"
    )

    for filepath in filepaths:
        filename = filepath.split("/")[-1]  # Get the filename from the path
        dest_filepath = f"{dest_folder}/{filename}"

        docx_file = str(dest_filepath.replace(".pdf", ".docx"))
        pdf_file = Converter(filepath)
        pdf_file.convert(docx_file)

        print(f"{filename} saved to {dest_folder}")
        output = str(f"{filename} saved to {dest_folder}")
        update_label(output, root)


def pdf_to_epub(root):
    global output
    global label
    filepaths = filedialog.askopenfilenames(initialdir="C:\\", title="Elige el archivo",
                                            filetypes=(("Documentos", "*.pdf"), ("all files", "*.*")))
    if len(filepaths) == 0:
        print("No files selected")
        output = str("No files selected")
        update_label(output, root)
        return

    dest_folder = filedialog.askdirectory(
        initialdir="C:\\",
        title="Selecciona el destino del archivo"
    )

    for filepath in filepaths:
        print(filepath)
        output = str(filepath)
        update_label(output, root)

        filename = filepath.split("/")[-1]  # Get the filename from the path
        dest_filepath = f"{dest_folder}/{filename}"

        epub_file = str(dest_filepath.replace(".pdf", ".epub"))
        pdf_file = aw.Document(filepath)
        pdf_file.save(epub_file)

        print(f"{filepath} saved as {dest_filepath.replace('.pdf', '.epub')}")
        output = str(f"{filepath} saved as {dest_filepath.replace('.pdf', '.epub')}")
        update_label(output, root)


def desbloquear_pdf(root):
    common.not_implemented(root)


def comprimir_pdf(root):
    common.not_implemented(root)


def pdf_a_power_point(root):
    common.not_implemented(root)


def epub_a_pdf(root):
    common.not_implemented(root)


def pdf_a_mobi(root):
    common.not_implemented(root)


def pdf_a_texto(root):
    common.not_implemented(root)


def epub_a_mobi(root):
    common.not_implemented(root)


def mobi_a_epub(root):
    common.not_implemented(root)
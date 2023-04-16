import subprocess
import os
import sys
import platform
from . import common_content as common

# lista de módulos que se necesitan instalar
required_modules = ["Pillow"]


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
    from moviepy.video.io.VideoFileClip import VideoFileClip
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


# Convert MP4 to GIF
def mp4_to_gif(root):
    global output
    global label
    filepaths = filedialog.askopenfilenames(initialdir="C:\\", title="Elige el archivo",
                                            filetypes=(("Archivos de vídeo", "*.mp4"), ("all files", "*.*")))
    if len(filepaths) == 0:
        print("No files selected")
        return
    dest_folder = filedialog.askdirectory(
        initialdir="C:\\",
        title="Selecciona el destino del archivo"
    )
    for filepath in filepaths:
        print(filepath)

        filename = filepath.split("/")[-1]  # Get the filename from the path
        dest_filepath = f"{dest_folder}/{filename}"

        # with open(dest_filepath, 'w') as file:
        #     file.write(content)
        nuevo = str(dest_filepath.replace(".mp4", ".gif"))
        video = VideoFileClip(filepath)
        video.write_gif(nuevo, fps=30)
        print(f"{filename} saved to {dest_folder}")
        output = str(f"{filename} saved to {dest_folder}")
        update_label(output, root)
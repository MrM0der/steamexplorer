import os
from tkinter import *
from tkinter import filedialog
print("""

█▀ ▀█▀ █▀▀ ▄▀█ █▀▄▀█   █▀▀ ▀▄▀ █▀█ █░░ █▀█ █▀█ █▀▀ █▀█
▄█ ░█░ ██▄ █▀█ █░▀░█   ██▄ █░█ █▀▀ █▄▄ █▄█ █▀▄ ██▄ █▀▄
""")
print("Steam Explorer by MrModer#1144")
print("Используй в Spacewar под названием SteamworksExample.exe")
print("Закрой это окно, чтобы выйти ;)")
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Steam Explorer",
                                          filetypes = (("EXE files",
                                                        "*.exe*"),
                                                       ("all files",
                                                        "*.*")))
      
    os.system(f'"{filename}"')

while True:
    browseFiles()

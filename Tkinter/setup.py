import sys
import os
from cx_Freeze import setup,  Executable


os.environ['TCL_LIBRARY'] = r'C:\Users\Ray\AppData\Local\Programs\Python\Python37\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ray\AppData\Local\Programs\Python\Python37\tcl\tk8.6'

include_files = []

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["webbrowser","datetime","requests","bs4","tkinter","SSL" ],"include_files": ["tcl86t.dll", "tk86t.dll"] ,"includes": ["idna.idnadata"], "optimize" :1,"excludes": [""] }



# GUI applications require a different base on Windows (the default is for a
# console application).

base = None
if sys.platform == "win32":
    base = "Win32GUI"
   # pass

setup(  name = "Fortnite News",
        version = "1.0",
        description = "Fortnite News",
        options = {"build_exe": build_exe_options},
        executables = [Executable("web_scraper.py",base = base)])

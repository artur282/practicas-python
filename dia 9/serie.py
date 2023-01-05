import os
import re


ruta = "C:\\Users\\Atlas\\Proyectos\\python\\curso python\\dia 9\\Mi_Gran_Directorio"
patron = r"[N]\D{3}-\d{5}"


for carpeta, subcarpeta, archivo in os.walk(ruta):

    for arch in archivo:
        if re.search(patron, arch):
            print(f"\t{arch}")

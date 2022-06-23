# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    resolution = re.search(r"(?<=<Resolution>)\s*<(\w)>\s*(\d*)\s*<.*>\s*<(\w)>\s*(\d*)\s*<.*>", texto)
    x = resolution[2]
    y = resolution[4]
    if resolution[1] != "X":
       x = resolution[4]
       y = resolution[2]
    return "Resolucion X: " + x + "\n" + "Resolucion Y: " + y

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = open(archivo_entrada, 'r')
    datos = f.read()
    f.close()
    salida = programa(datos)
    f = open(archivo_salida, 'w')
    f.write(salida)
    f.close()

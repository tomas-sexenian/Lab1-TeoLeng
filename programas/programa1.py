# -*- coding: utf-8 -*-
import re
import sys

# regex para sacar fecha y hora ^(19|20)\d\d-(0[1-9]|1[012])-([012]\d|3[01])T([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$
# ejemplo de entrada 2022-03-17T15:25:15.000+00:00
# ejemplo de salida 15:25 del 2022-03-17

def programa(texto):
    resolution = re.search(r"(?<=<FileModifyDate>) \s*(\d*-\d*-\d*)T(\d*:\d*)",texto)
    fecha = resolution[1]
    hora = resolution[2]
    return hora + " del " + fecha

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

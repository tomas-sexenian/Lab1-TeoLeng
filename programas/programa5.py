# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    solution1 = re.sub(r"<\w*>(\s*\d+\.?\d*\s*)\s*<\/(\w*)>","",texto)
    solution2 = re.sub(r"<\w*><\/(\w*)>","",solution1)
    solution3 = re.sub(r"<\w*>(\s)*(\n)*(\s)*<\/(\w*)>","",solution2)
    solution4 = re.sub(r"^(\s)+(\n)","",solution3)
    solution5 = re.sub(r"^(\s)*$","",solution4)
    solution6 = re.sub(r"(\n)(\n)","\n",solution5)
    solution7 = re.sub(r"(\n)(\s)*(\n)","\n",solution6)
    return solution7

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

# -*- coding: utf-8 -*-
import re
import sys

def programa(texto):
    matches = re.findall(r"<([^\/]*)>\n*.*(https*\:\/\/.*(?!\.uy)\.\w+[\/\s].*)\n*<\/.*>", texto)
    
    solution = ""

    for i in range(len(matches)):
        solution = solution + matches[i][0] + " -- " + matches[i][1].strip()
        
        if i < len(matches)-1:
            solution =  solution + "\n"

    return solution

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

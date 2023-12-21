"""
# lectura de archivo

with open("data/movimientos.csv","r") as resultado:
    leer = resultado.read()
    
    print(type(leer))

#otro ejemplo de lectura de archivos css
    
resultado = open("data/movimientos.csv","r")
lectura = resultado.readlines()
print(lectura)
"""
import csv

midato= []
mifichero = open('data/movimientos.csv', 'r')
lectura = csv.reader(mifichero,delimiter=",",quotechar='"')
for items in lectura:
    print(type(items))
    midato.append(items)

print("mi lista: ", midato[0][1])
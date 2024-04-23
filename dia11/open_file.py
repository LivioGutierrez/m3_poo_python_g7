"""
funcion OPEN
file= open(ruta,argumento/modo de apertura) ->retorna un objeto de type file
"""
import os
try:
    log_file= open(os.path.abspath("dia11/logs/error.log"))#<_io.TextIOWrapper name='C:\\Users\\Nico\\TalentoDigital\\2024\\0044-1\\MODULO_POO\\dia11\\logs\\error.log' mode='r' encoding='cp1252'>
    print(log_file)
    print(type(log_file))
except FileNotFoundError as fnfe:
    print("Archivo o directorio no encontrado")
    #print(fnfe) -> [Errno 2] No such file or directory: 'C:\\Users\\Nico\\TalentoDigital\\2024\\0044-1\\MODULO_POO\\logs\\error.log'

#ARGUEMNTOS
log_file2= open(os.path.abspath("dia11/html/index.html"),"r")
print(log_file2.read())
log_file2.close()

print("************READLINE*********************\n")
log_file3= open(os.path.abspath("dia11/html/index.html"),"r")
print(log_file3.readline())#trabajar con for para leer linea a linea
log_file3.close()

print("***********READLINES*****************\n")
log_file4= open(os.path.abspath("dia11/html/index.html"),"r")
print(log_file4.readlines())#agrega una lista de cada una de las lineas
log_file4.close()
print("")

print("***********WITH*****************\n")
with open(os.path.abspath("dia11/html/index.html"),"r")as archivo:
    #print(archivo) -> <_io.TextIOWrapper name='C:\\Users\\Nico\\TalentoDigital\\2024\\0044-1\\MODULO_POO\\dia11\\html\\index.html' mode='r' encoding='cp1252'>
    for linea in archivo:
        #print(linea)
        print(linea.strip())

#ARGUMENTOS w, SOLO ESCRITURA
#La ruta donde se creara el archivo debe existir
log_file5= open(os.path.abspath("dia11/html/assets/css/style.css"),"w")
log_file5.write("/*Esto es un comentario*/\n")
log_file5.write(" * {\n\tmargin:0px\n} ")
log_file5.close()

import time
try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"dia11/logs/{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
    
import math

'''
Cifrado - Transposición por columnas con clave

Autores:
    Cristian Valeriano Barrios
    Gerardo Salinas Gutierrez
'''

print("\n----------------------------------------",
      "\nSegunda capa - T. por columnas con clave",
      "\n----------------------------------------")

'''
Lectura del mensaje y la clave
'''

#archivo abierto en modo lectura
f = open("mensaje.txt","r")
if f.mode == "r":
    mensaje = f.read() #se guarda el mensaje leído 
print("\nMensaje leído:", mensaje.upper())
f.close() #cierre del archivo

mensaje = mensaje.replace(' ', '').upper() #se elimina cualquier espacio y se convierte en mayúsculas

#ingresamos la clave, esta debe tener caracteres NO repetidos
clave = str(input("\nIntroduce la clave sin repetir letras: ")) 
clave = clave.replace(' ', '').upper() #se elimina cualquier espacio y se convierte en mayúsculas

'''
Proceso de cifrado
'''
# Los caracteres de Mcla se acomodan en un determinado número de columnas.
# Escribiendo el Mcla en forma horizontal de izquierda a derecha (no. de columnas depende del no. de caracteres de la palabra clave).
# Nota: Todas las columnas deben contener el mismo número de caracteres, en caso contrario se completan éstas con X para cumplir la condición.
# El ordenamiento de las columnas dependerá del ordenamiento alfabético de los caracteres de dicha palabra.

print("\n------------------",
      "\nProceso de cifrado",
      "\n------------------\n")

msgLength = len(mensaje) #tamaño del mensaje a cifrar
msgList = list(mensaje)

print(msgList)

columnas = len(clave)
filas = int(math.ceil(msgLength/columnas))

vacio = int((filas*columnas) - msgLength)
msgList.extend('X' * vacio)

cifrado = ['']*columnas

for columna in range(columnas):
    i = columna
    while i < len(msgList):
        cifrado[columna] += msgList[i]
        i += columnas
print(cifrado)

keyPointer = 0
keylist = sorted(list(clave))
textoCifrado = ""

for i in range(columnas):
    curr = clave.index(keylist[keyPointer])
    textoCifrado += ''.join(cifrado[curr])
    keyPointer += 1

print(textoCifrado)        

#archivo abierto en modo escritura
f = open("mensajecifrado.txt","w")
if f.mode == "w":
    f.write(textoCifrado) #se guarda el mensaje cifrado 
    print("\nMensaje cifrado guardado exitosamente en 'mensajecifrado.txt'")
f.close() #cierre del archivo
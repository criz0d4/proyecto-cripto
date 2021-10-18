import math

'''
Cifrado - Transposición por columnas con clave

Autores:
    Cristian Valeriano Barrios
    Gerardo Salinas Gutierrez
'''

# Segunda capa: Columnas

# Los caracteres de Mcla se acomodan en un determinado número de columnas.
# Escribiendo el Mcla en forma horizontal de izquierda a derecha (no depende del no. de caracteres de la palabra clave).
# Nota: Todas las columnas deben contener el mismo número de caracters, en caso contrario se completan éstas con X para cumplir la condición.
# El ordenamiento de las columnas dependerá del ordenamiento alfabético de los caraccteres de dicha palabra.

print("\n----------------------------------------",
      "\nSegunda capa - T. por columnas con clave",
      "\n----------------------------------------")

#archivo abierto en modo lectura
f = open("mensajecifrado.txt","r")
if f.mode == "r":
    mcifrado = f.read() #se guarda el mensaje leído 
print("\nMensaje leído:", mcifrado.upper())
f.close() #cierre del archivo

mcifrado = mcifrado.replace(' ', '').upper()	 
clave = str(input("\nIntroduce la clave: "))
clave = clave.replace(' ', '').upper()	

# Desifrado
print("\n---------------------",
      "\nProceso de descifrado",
      "\n---------------------")


msgLength = len(mcifrado)
msgList = list(mcifrado) 
  
columnas = len(clave) 
     
filas = int(math.ceil(msgLength / columnas)) 
  
descifrado = [] 
for i in range(filas):
    descifrado += [[''] * columnas]
    
keyPointer = 0
msgPointer = 0
keyList = sorted(list(clave))
  
for i in range(columnas): 
    curr = clave.index(keyList[keyPointer])
    for j in range(filas):
        descifrado[j][curr] = msgList[msgPointer]
        msgPointer += 1
    keyPointer += 1

msg = ""

for i in range(filas):
    msg += ''.join(descifrado[i])
  
emptyCounter = msg.count('x') 
  
if emptyCounter > 0: 
    print (msg[: -emptyCounter] )
  
#return msg 
print("\nMensaje descifrado por Transposición",
      "\npor columnas con clave:\n->", msg)       
import math

'''
Descifrado - Transposición por columnas con clave

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
f = open("mensajecifrado.txt","r")
if f.mode == "r":
    mcifrado = f.read() #se guarda el mensaje leído 
print("\nMensaje leído:", mcifrado.upper()) #se convierte en mayúsculas
f.close() #cierre del archivo

mcifrado = mcifrado.replace(' ', '').upper()	 

#ingresamos la clave
clave = str(input("\nIntroduce la clave: "))
clave = clave.upper() #se convierte en mayúsculas

'''
Proceso de descifrado
'''
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
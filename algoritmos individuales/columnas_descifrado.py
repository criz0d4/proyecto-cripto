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

msgLength = len(mcifrado) #tamaño del mensaje a descifrar
msgList = list(mcifrado) #el mensaje se divide en elementos de una ['L', 'I', 'S', 'T', 'A']
  
columnas = len(clave) #se determina el número de columnas según el tamaño de la clave
filas = int(math.ceil(msgLength/columnas)) #se calculan las filas, math.ceil devuelve el entero mayor o más próximo de la división del msgLength/columnas
  
descifrado = [] #se crea la variable de la matriz de descifrado

for i in range(filas): 
    descifrado += [[''] * columnas] #se crea la matriz de descifrado
        
claveApuntador = 0 #variable del apuntador de la clave
mensajeApuntador = 0 #variable del apuntador del mensaje
claveOrdenada = sorted(list(clave)) #la clave se divide en elementos de una lista y se ordena alfabéticamente
   
for i in range(columnas): #se busca la columna
    posicionClave = clave.index(claveOrdenada[claveApuntador]) #'posicionClave' contiene la posición en la lista de cada letra de la clave ordenada en la clave original
    for j in range(filas): #se busca por fila dentro de la columna
        descifrado[j][posicionClave] = msgList[mensajeApuntador] #fila columna por columna según posicionClave
        mensajeApuntador += 1 #el apuntador se incrementa para continuar con la siguiente fila
    claveApuntador += 1 #el apuntador se incrementa para continuar con la siguiente columna

mensaje = "" #variable donde se guardará el mensaje cifrado

for i in range(filas):
    mensaje += ''.join(descifrado[i]) #se escribe en la cadena mensaje el contenido de las filas de la matriz de descifrado

print("\nMensaje descifrado por Transposición",
      "\npor columnas con clave:\n->", mensaje)       
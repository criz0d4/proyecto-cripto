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
msgList = list(mensaje) #el mensaje se divide en elementos de una ['L', 'I', 'S', 'T', 'A']

columnas = len(clave) #se determina el número de columnas según el tamaño de la clave
filas = int(math.ceil(msgLength/columnas)) #se calculan las filas, math.ceil devuelve el entero mayor o más próximo de la división del msgLength/columnas

#en caso de haber espacios vacíos
vacios = int((filas*columnas) - msgLength) #se determina el número de espacios vacios. Será el resultado de filas*columnas menos el tamaño del mensaje
msgList.extend('X' * vacios) #.extend incrementa el núemero de elementos en la lista con 'X' según el número de espacios vacíos

cifrado = ['']*columnas #se crea la matriz para el mensaje cifrado

for columna in range(columnas): #escritura del mensaje cifrado
    i = columna
    while i < len(msgList): #mientras i sea menor al tamaño de la lista del mensaje
        cifrado[columna] += msgList[i] #se agrega caracter por caracter de la lista en la columna correspondiente
        i += columnas #sumando número de las columnas, avanzamos ese número de posiciones en la lista. Así, nos colocamos en la fila de abajo y continúa el ciclo.
    
claveApuntador = 0 #variable del apuntador de la clave
claveOrdenada = sorted(list(clave)) #la clave se divide en elementos de una lista y se ordena alfabéticamente

textoCifrado = "" #variable donde se guardará el mensaje cifrado

for i in range(columnas):   
    #'posicionClave' contiene la posición en la lista de cada letra de la clave ordenada en la clave original
    posicionClave = clave.index(claveOrdenada[claveApuntador]) #clave.index hace la búsqueda en la clave original    
    textoCifrado += ''.join(cifrado[posicionClave]) #se escribe en la cadena textoCifrado el contenido de la columna determinada por posicionClave dentro de la matriz de cifrado
    claveApuntador += 1 #el apuntador se incrementa para continuar con la siguiente columna
  
#archivo abierto en modo escritura
f = open("mensajecifrado.txt","w")
if f.mode == "w":
    f.write(textoCifrado) #se guarda el mensaje cifrado 
    print("Mensaje cifrado guardado exitosamente en 'mensajecifrado.txt'")
f.close() #cierre del archivo
'''
Cifrado - Afín

Autores:
    Cristian Valeriano Barrios
    Gerardo Salinas Gutierrez
'''

print("\n-------------------",
      "\nTercera capa - Afín",
      "\n-------------------")

'''
Lectura del mensaje, constantes de decimación y de desplazamiento
'''

alfabeto= 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ' #alfabeto de 27 caracteres
cifrado = '' 
n = len(alfabeto)

#archivo abierto en modo lectura
f = open("mensaje.txt","r")
if f.mode == "r":
    mclaro = f.read() #se guarda el mensaje leído 
print("\nMensaje leído:", mclaro.upper())
f.close() #cierre del archivo

mclaro = mclaro.replace(' ', '').upper() #se elimina cualquier espacio y se convierte en mayúsculas

a = int(input("\nIngrese la constante de decimación (a): ")) #ingresar a 
b = int(input("Ingrese la constante de desplazamiento (b): ")) #ingresar b

'''
Proceso de cifrado
'''
# C(i)=(a*Mi+b)mod(n)

print("\n------------------",
      "\nProceso de cifrado",
      "\n------------------")

#condición para la constante de desplazamiento   
if b>n or b<0:
    b=b%n
 
#lectura letra por letra del mensaje
for i in mclaro: 
    #alfabeto.find(i) por cada caracter leído, encuentra su posición dentro del alfabeto
    x=a*alfabeto.find(i)+b #se realiza la operación (a*Mi+b)
    cifrado+=alfabeto[x%n] #se aplica el mod(n) dentro de alfabeto[] para encontrar el caracter según la posición    

#archivo abierto en modo escritura
f = open("mensajecifrado.txt","w")
if f.mode == "w":
    f.write(cifrado) #se guarda el mensaje cifrado 
    print("\nMensaje cifrado guardado exitosamente en 'mensajecifrado.txt'")
f.close() #cierre del archivo
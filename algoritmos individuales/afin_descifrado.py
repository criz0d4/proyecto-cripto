'''
Descifrado - Afín

Autores:
    Cristian Valeriano Barrios
    Gerardo Salinas Gutierrez
'''

print("\n-------------------",
      "\nTercera capa - Afín",
      "\n-------------------")

alfabeto= 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ' #alfabeto de 27 caracteres
n = len(alfabeto)
descifrado = ''

#archivo abierto en modo lectura
f = open("mensajecifrado.txt","r")
if f.mode == "r":
    mcifrado = f.read() #se guarda el mensaje leído 
print("Mensaje leído:", mcifrado)
f.close() #cierre del archivo

a = int(input("\nIngrese la constante de decimación (a): ")) #ingresar a 
b = int(input("Ingrese la constante de desplazamiento (b): ")) #ingresar b

# Descifrado
# Mi = (Ci*a^-1)mod(n) 
# a1 es el a^(-1)

for a1 in range(0,n): # mínimo común divisor
    if (a1*a)%n==1:
        break

print("El valor de a =", a, "el valor de a^-1 =", a1)

#lectura letra por letra del mensaje
for i in mcifrado: 
    #alfabeto.find(i) por cada caracter leído, encuentra su posición dentro del alfabeto
    x=a1*(alfabeto.find(i)-b) #se realiza la operación (a*Mi-b)
    descifrado+=alfabeto[x%n] #se aplica el mod(n) dentro de alfabeto[] para encontrar el caracter según la posición 
    
print("\n---------------------",
      "\nProceso de descifrado",
      "\n---------------------")

print("\nMensaje descifrado por Afín:\n->", descifrado)
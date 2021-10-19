#! /usr/bin/python


print ("que está pasando")

a='12345'
b='concatenar'

print(b*len(a))

def cifrar(clave, datos):

    n = len(datos)

    if len(clave) != n:
        print("Error: la longitud de clave y los datos no coincide.")
        return
    
    resultado = []

    for i in range(0, n):
        resultado.append(clave[i] ^ datos[i])

    return resultado

cifrar('contraseña','texto')
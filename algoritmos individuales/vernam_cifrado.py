#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
Cifrado - Afín
Autores:
    Cristian Valeriano Barrios
    Gerardo Salinas Gutierrez
'''
import os
import binascii
import random
import string
import sys
from operator import xor

#mCla = 'everything' #Cadena de prueba

f = open("mensaje.txt","r")
if f.mode == "r":
    mCla = f.read() #se guarda el mensaje leído 
print("\nMensaje leído:", mCla)
f.close() #cierre del archivo

mCla = mCla.replace(' ', '').upper() #se elimina cualquier espacio y se convierte en mayúsculas

def cifrado(mCla):

	###	Generando clave única
	n = len(mCla)	#Longitud del mCla para generar una máscara de la misma longitud
	key = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(n))	#Genera una clave aleatória
	key_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in ascii(key)) #Convierte la clave a ASCII y luego a binario
	
	### Conversión del mensaje
	mensaje_ascii = ascii(mCla) #Convierte el mensaje a su equivalente ASCII
	mensaje_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mensaje_ascii) #Convierte el mensaje a binario
	
	#Asegurando que mCla y clave sean del mismo tipo (string)
	mensajeStr = str(mCla)
	keyStr = str(key)

	#Guardando la clave en un txt, para que pueda ser usada en el descifrado
	f = open("clave.txt","w")
	if f.mode == "w":
		f.write(keyStr) #se guarda la contraseña
		print("\nClave guardada exitosamente en 'clave.txt'")
		f.close() #cierre del archivo

	print ('Mensaje original: ' + mensajeStr)
	print ('Key: ' + keyStr)
	

	cifrado = '' #inicializando variable 

	#Proceso de cifrado = (mCla) XOR (key)
	for i, c in enumerate(mensajeStr, start=0):	#Recorre el mensaje caracter a caracter
		aux_xor = xor(ord(mensajeStr[i]), ord(keyStr[i]))	#Operación XOR entre cada par de caracteres
		cifrado += chr(aux_xor)	#Guardando el resultado de la operación en la cadena "cifrado"

	#cifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in cifrado)	#Se pasa el cifrado obtenido a binario y se guarda como string

	#print ('Mensaje cifrado en binario: ' + cifrado_binario)
	print ('Mensaje cifrado: ' + cifrado)
	print ()

	#Guardando el mensaje cifrado en un txt
	f = open("vernam.txt","w")
	if f.mode == "w":
		f.write(cifrado) #se guarda el mensaje cifrado 
		print("\nMensaje cifrado guardado exitosamente en 'vernam.txt'")
	f.close() #cierre del archivo

cifrado(mCla)

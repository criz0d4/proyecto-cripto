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

def descifrado():

	#Abriendo el txt donde está el mensaje cifrado
	f = open("vernam.txt","r")
	if f.mode == "r":
		mensajeStr = f.read() #se guarda el mensaje leído en un string
		print("\nMensaje leído:", mensajeStr)
	f.close() #cierre del archivo
	
	#Abriendo el txt donde está guardada la clave generada en el cifrado
	f = open("clave.txt","r")
	if f.mode == "r":
		keyStr = f.read() #se guarda la clave en un string 
		print("\nClave leída:", keyStr)
	f.close() #cierre del archivo

	cifrado = ''	#Inicializando la variable "cifrado"

	for i, c in enumerate(mensajeStr, start=0):	#Recorre el mensaje caracter a caracter
		aux_xor = xor(ord(mensajeStr[i]), ord(keyStr[i]))	# XOR entre cada par de caracteres
		cifrado += chr(aux_xor)	#Guardando el resultado de la operación en la cadena "cifrado"

	#cifrado_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in cifrado)	# Se pasa el cifrado obtenido a binario y se guarda como string

	#print ('Mensaje descifrado en binario: ' + cifrado_binario)
	print ('Mensaje descifrado: ' + cifrado)
	print ()


descifrado()
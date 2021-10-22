#! /usr/bin/python3
# -*- coding: utf-8 -*-

#############################################
#	Autores:
#		Cristian Valeriano Barrios
#		Gerardo Salinas Gutierrez
#############################################
#	POGRAMA DE CIFRADO
#
#		Primera Capa: T. POR COLUMNAS
#		Segunda Capa: AFIN
#		Tercera Capa: VERNAM
#############################################

import time

'''
Menú del programa
'''
from verificador import verifica_mCla
from verificador import verifica_vernam_clave

print("CRIPTOGRAFÍA\n\nElaborado por:\n\tSalinas Gutiérrez Gerardo\n\tValeriano Barrios Cristian")
print("\n¡BIENVENIDO AL PROGRAMA DE CIFRADO!\n")

def menu():

	print("\nPor favor, teclée el número correspondiente a su elección:")
	o = int(input("\n	(1) Cifrar Mensaje.\n	(2) Descifrar Criptograma.\n	(3) Salir.\n\n"))

### ________________________________________
###	

	if o == 1:
		print("\nVerificando que exista el archivo: 'mensaje.txt'...\n")
		if verifica_mCla() == True :
      
			from columnas_cifrado import textoCifrado
			print("\nPrimera etapa completada")
			time.sleep(1)
   
			from afin_cifrado import cifrado
			print("\nSegunda etapa completada")
			time.sleep(1)

			from vernam_cifrado import cifrado
			time.sleep(1)
			print("\nTercera etapa completada")
			time.sleep(2)
			menu()
   
		else:
			menu()


	elif o == 2:
		print("\nVerificando que existan los archivos 'mensajecifrado.txt' y 'clave.txt'...\n")
		if verifica_vernam_clave() == True :
			from vernam_descifrado import descifrado
			time.sleep(1)

			from afin_descifrado import descifrado
			print("Afin", descifrado)
			time.sleep(1)
   
			from columnas_descifrado import mensaje
			print("\nEl mensaje original es: ", mensaje,
					"\n----------------------")
			time.sleep(1)
			print("\n¡Hasta pronto!\n")
			time.sleep(5)
	
		else:
			menu()


	elif o == 3:
		print("\n¡Hasta pronto!\n")
		exit()

	else:
		print("\nOpción incorrecta.")
		menu()

menu()




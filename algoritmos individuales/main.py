#! /usr/bin/python3
# -*- coding: utf-8 -*-

#############################################
#	Autores:
#		Cristian Valeriano Barrios
#		Gerardo Salinas Gutierrez
#############################################
#	POGRAMA DE CIFRADO
#
#		Primera Capa: VERNAM
#		Segunda Capa: T. POR COLUMNAS
#		Tercera Capa: AFIN
#############################################

'''
Menú del programa
'''
from verificador import verifica_mCla
from verificador import verifica_vernam_clave

print("\n\n¡BIENVENIDO AL PROGRAMA DE CIFRADO!\n")

def menu():

	print("\nPor favor, teclée el número correspondiente a su elección:\n")
	o = int(input("\n	(1) Cifrar Mensaje.\n	(2) Descifrar Criptograma.\n	(3) Salir.\n\n"))

### ________________________________________
###	

	if o == 1:
		print("\nVerificando que exista el archivo: 'mensaje.txt'...\n")
		if verifica_mCla() == True :
			from vernam_cifrado import cifrado
		else:
			menu()


	elif o == 2:
		print("\nVerificando que existan los archivos 'vernam.txt' y 'clave.txt'...\n")
		if verifica_vernam_clave() == True :
			from vernam_descifrado import descifrado
		else:
			menu()




	elif o == 3:
		print("\n¡Hasta pronto!\n")
		exit()

	else:
		print("\nOpción incorrecta.")
		menu()

menu()




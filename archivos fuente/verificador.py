#! /usr/bin/python3
# -*- coding: utf-8 -*-

#############################################
#	Autores:
#		Cristian Valeriano Barrios
#		Gerardo Salinas Gutierrez
#############################################
import os

def verifica_mCla():
	if os.path.isfile('mensaje.txt'):
		print("Correcto. \nCifrando mensaje...\n")
		return True
	else:
		print ("El archivo no existe, regresando al menú...\n")
		return False


def verifica_vernam_clave():
	if ( os.path.isfile('mensajecifrado.txt') and os.path.isfile('clave.txt') ):
		print("Correcto....\n")
		return True
	else:
		print ("Los archivos no existen, imposible descifrarlo...\n")
		return False


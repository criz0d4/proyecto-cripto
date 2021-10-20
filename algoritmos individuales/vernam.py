#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import binascii

print ("que está pasando")


def generar_clave(mCla):

    key =  binascii.hexlify(os.urandom(len(mCla))).decode()
    print ('Clave: ' + key)

    key_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in key)	# Se pasa la clave a binario y se guarda como string
    print ('Clave en binario: ' + key_binario)

def cifrar(mCla):

	#mensaje_binario = ''.join(bin(ord(x))[2:].zfill(8) for x in mCla)	# Se pasa el mensaje a binario y se guarda como string
	mensaje_binario = binascii(mCla).decode()
	print ('Mensaje original en binario: ' + mensaje_binario)


generar_clave('astro')

cifrar('astro')

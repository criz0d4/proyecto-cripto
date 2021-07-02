################################
#	Autores:
#	Cristian Valeriano Barrios
#	Gerardo Salinas Gutiérrez
################################
#	Primera Capa: T. por grupos
#	Segunda Capa: Afin
#	Tercera Capa: Playfair
################################

def main():

	f = open("mensaje.txt","r")
	#print ('Mensaje en claro: ')
	if f.mode == "r":
		mclaro = f.read()
		print('Mensaje en claro: ', mclaro)
	f.close()
	#Llamada a funcion de transposicion: 
	t_groups(mclaro)


def t_groups(mclaro):
	#Quitando espacios y el \n del archivo:
	t_mclaro = mclaro.replace(" ", "").replace("\n","")
	print(t_mclaro)
	#Longitud de la cadena
	n = len(t_mclaro)
	print ('Len:',n)
	#Separando en substrings (grupos)
	p = 0
	group = { }
	for i in range(0,n-1,5):
		group[p] = t_mclaro[i:i+5]
		print(group[p]),
		p=p+1
	print('\n')
	#Aplicando el cifrado 01234=10243
	group2 = { }
	for i in range(0,p):
		temp = group[i]
		group2[i] = temp[1:2] + temp[0:1] + temp[2:3] + temp[4:5] + temp[3:4]
		print(group2[i]),

if __name__=="__main__":
	main()
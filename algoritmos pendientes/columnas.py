# Segunda capa: Columnas

# Los caracteres de Mcla se acomodan en un determinado número de columnas.
# Escribiendo el Mcla en forma horizontal de izquierda a derecha (no depende del no. de caracteres de la palabra clave).
# Nota: Todas las columnas deben contener el mismo número de caracters, en caso contrario se completan éstas con X para cumplir la condición.
# El ordenamiento de las columnas dependerá del ordenamiento alfabético de los caraccteres de dicha palabra.

def main():
    
    f = open("mensaje.txt","r")
    if f.mode == "r":
        mclaro = f.read()
        print("Mensaje en claro:", mclaro)
    f.close()
  
    key = input("Ingrese la clave ")
    print("La clave es:", key)
    len_key = len(key)
    print("El tamaño es: ", len_key)
    
    print(list(sorted(key).index(char) for char in key))
  #  encrypt_columnas(mclaro)

# def encrypt_columnas(mclaro):



if __name__=="__main__":
	main()
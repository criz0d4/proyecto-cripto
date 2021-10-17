# Tercera capa: Afín

def main():
    
    '''
    f = open("mensaje.txt","r")
    if f.mode == "r":
        mclaro = f.read()
        print("Mensaje en claro:", mclaro)
    f.close()
    '''
    
    mclaro = "lapiz"
  
    a = input("Ingrese la constante de decimación ")
    b = input("Ingrese la constante de desplazamiento ")
    n = input("Ingrese el orden del grupo ")
    
    print("\nLa constante de decimación es:", a)
    print("La constante de desplazamiento es:", b)
    print("El orden del grupo es de", n)
    
    afin(mclaro, a, b, n)

def afin(mclaro, a, b, n):
    print("\nProceso de cifrado:\nEl mensaje en claro es:", mclaro,
          ", constante de decimación =", a,
          ", constante de desplazamiento =", b)






if __name__=="__main__":
	main()
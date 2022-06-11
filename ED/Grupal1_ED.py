

#a) Procesamiento inicial de la información:

def AbrirFichero (nombre_fichero):

    lista = []

#Este bucle elimina los saltos de línea del fichero y almacena cada palabra 
#como un elemento de una lista, si bien no depura los posibles signos de 
#puntuación que puedan contener las palabras almacenadas.

    for linea in nombre_fichero:     #Eliminamos los saltos de linea (\n y \r)
        if (linea[-1] == "\n"):
            linea = linea [:len (linea) -1]
            if (linea[-1] == "\r"):
                linea = linea [:len (linea) -1]

        lista += linea.split (" ")    #Añadimos la linea modificada a la lista

    return lista


#b)

#La siguiente función recibe una lista y elimina los signos de puntuación de 
#los elementos de dicha lista.

#Los signos de puntuación ",", "." y ";" siempre aparecerán al final de cada 
#palabra, de modo que la función elimina este último elemento de cada string
#cuando es necesario. Los elementos (tanto si han requerido modificación como
#si no) se almacenan en una nueva lista (lista2 en la función).

def EliminarPuntuacion (lista):

    lista2 = []     #Lista para añadir las palabras sin signos de puntuacion

    for palabra in lista:     #Buscamos todas las palabras de la lista

        if palabra[-1:]== "," or palabra[-1:]=="." or palabra[-1:]==";":

            lista2.append (palabra [:len (palabra) -1])                                         #Añadimos a la lista la palabra sin el signo de puntuacion al final

        else:
            lista2.append (palabra)
    return lista2

#EliminarRepetidos debuelve una lista del conjunto de elementos de una lista
    
def EliminarRepidos (lista):
    lista_sin_rep = set(lista)    
    
    return lista_sin_rep


def main():

    #a)

    print("Leer fichero de texto y poner todas las palabras en una lista")

    #Abrimos el archivo a procesar:

    fichero = open ("Prueba.txt", "r")    

    #Almacenamos el fichero de texto en una lista con la función AbrirFichero:

    fichero_modificado = AbrirFichero(fichero)

    #Este print imprime en pantalla la lista generada por la función AbrirFichero: 
    print (fichero_modificado)

    #b)

    #La función EliminarPuntuación recogerá la lista anterior y eliminará los signos de puntuación que
    #puedan contener los elementos. 

    lista_sin_signos = EliminarPuntuacion(fichero_modificado)

    #Este print imprime en pantalla la lista de palabras sin signos de puntuación.
    print(lista_sin_signos)

    listaFinal = list(dict.fromkeys(lista_sin_signos))

    print(listaFinal)

    ficheroFinal = open("FicheroFinal.txt", "w")
    
    for palabra in listaFinal:
        ficheroFinal.write(palabra)

    ficheroFinal.close()



if __name__ == "__main__":
    main()

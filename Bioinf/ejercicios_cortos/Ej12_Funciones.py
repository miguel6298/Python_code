print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

def frec_matriz (Lseq): 

    dicc_nt = {"A":0,"C":1,"G":2,"T":3} #Primero se hace un diccionario con los nucleótidos como claves y la posición de la fila en la matriz como valor.
    frec_matrix = []
    secuence_list = [0] # Se crea la matriz de frecuencias  y una lista donde iran las posiciones de las secuencias.
    max_len = len(max(Lseq,key=len)) #Se calcula la longitud de la secuencia mas larga.

    for i in range(4): #Se introducen en la matriz cuatro listas con la longitud máxima entre todas las cadenas.
        frec_matrix.append(secuence_list*(max_len)) 

    for seq in Lseq: #Se recorre la lista con todas las secuencias.
        for pos in range((len(seq))): #Se recorren las posiciones de cada secuencia.
            frec_matrix[dicc_nt[seq[pos]]][pos]+=1
            #Se suma uno por cada vez que aparezca un determinado nucleótido en la posicion de la matriz correcta.

    return(frec_matrix)

sec = ["AGC", "GTT", "ATT", "GGG"]
print (frec_matriz(sec))
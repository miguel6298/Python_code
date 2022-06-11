print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

def matriz_codones():
    nucleotidos = "UCAG"
    ncol = 4
    nfil = 16
    lista = []

    for letter1 in nucleotidos:
        for letter2 in nucleotidos:
            for letter3 in nucleotidos:
                codon = letter1 + letter2 + letter3
                lista.append (codon)

    def lst_to_matrix(lst, groups): #Un poco de trampa, esto es para hacer una lista de listas. Preguntar al profesor con matrices.
        matrix = []
        for i in range (0, len(lst), groups):
            matrix.append (lst [i: i + groups])

        return matrix

    matriz = lst_to_matrix (lista, 4)
    

    for i in range (nfil):
        if i % 4 == 0:
            print ("-" * 15)
        for j in range (ncol):
            print (matriz[i][j], end=" ")   
        print ()
    print ("-" * 15)

    return 

matriz_codones()
print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

def matriz_codones():
    nucleotidos = ["A", "U", "G", "C",]
    nucleotidosT = nucleotidos * 4
    matriz = [] 
    ncol = 4
    nfil = 16
   
    for l in range (nfil):
        matriz.append ([0] * ncol)

    for i, fila in enumerate (nucleotidosT):
        for j, columna in enumerate (nucleotidos):
            for k, elemento in enumerate (nucleotidos):
                matriz [i][j][k] = fila + columna + elemento

    return matriz

print (matriz_codones())


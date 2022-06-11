print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

"""ntA = secuencia.count ("A")
    ntT = secuencia.count ("T")
    ntU = secuencia.count ("U")
    ntG = secuencia.count ("G")
    ntC = secuencia.count ("C")"""

def cuenta_nucleotidos (secuencia):
    ntA = ntT = ntU = ntG = ntC = 0
    diccionario = {}

    for i in secuencia: #Esta forma sería más económica para el ordenador porque solo hace una lectura (?)
        if i == "A":
            ntA += 1
        elif i == "T":
            ntT += 1
        elif i == "U":
            ntU += 1
        elif i == "G":
            ntG += 1
        elif i == "C":
            ntC += 1


    #Para devolver los resultados lo mejor sería un diccionario porque se puede indexar de una forma más intuitiva:
    
    diccionario = {
                "A": [ntA],
                "T": [ntT],
                "U": [ntU],
                "G": [ntG],
                "C": [ntC]
                }
    return diccionario

secuencia1 = "CGATAAACGATACGATCAGACTTTTACGGACG"
a = cuenta_nucleotidos(secuencia1)
print (a)




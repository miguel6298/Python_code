print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

def cuenta_codones (secuencia, codon):
    contador = 0
    triplete = []
    for nt in range (0, len(secuencia), 3):
        triplete = secuencia[nt: nt+3]
        if triplete == codon:
            contador += 1
    return contador

fichero = open ("candida.fa", "r") 
secuencia = fichero.read()


print (cuenta_codones (secuencia, "AAA"))
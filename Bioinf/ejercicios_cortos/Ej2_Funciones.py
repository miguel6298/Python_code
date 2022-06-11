print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

def cuenta_nucleotido (sec, nt):
    for i in sec:
        contador = sec.count (nt)
    return contador

sec1 = "AGCTACGTACGAGAGCTTACGATCATGACCAGATC"

print (cuenta_nucleotido (sec1, "A")) #Para ver el valor del return hay que hacer un print de la función con los argumentos.




print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()
print ("Bienvenido/a. Este programa sintetizará la proteína resultante contenida en una secuencia de ARN solicitada por teclado.")

proteina = '' 
codigoGenetico = {  #Diseñamos el diccionario que incluye el código genético.
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                 
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'-', 'UAG':'-',
    'UGC':'C', 'UGU':'C', 'UGA':'U', 'UGG':'W',
    }       

mRNA = input ("Por favor, introduzca la cadena de RNA: ") 
mRNA = mRNA.upper ()

#Comprobar RNA
comprobar_rna = mRNA.count("A") + mRNA.count("C") + mRNA.count("G") + mRNA.count("U")

if len(mRNA) != comprobar_rna:
    print ()
    print ("Error. La secuencia introducida no es RNA.")

else:
    #Buscamos el codón de inicio. 
    inicio = mRNA.find ("AUG")

    if inicio == -1:
        print ()
        print ("No se ha encontrado codón de inicio en la secuencia de RNA.")

    else: 
        CDS = mRNA [inicio:] #Para que la secuencia a traducir comience en el codón de inicio.
        codonesParada = ["UAG", "UAA", "UGA"]
        parada = False
        print ()

        try:
            for i in range (0, len(CDS), 3): #Para que recorra desde el codón de inicio hasta el final de 3 en 3.
                codon = CDS [i:i+3]
                proteina += codigoGenetico[codon]

                if codon == codonesParada[0] or codon == codonesParada[1] or codon == codonesParada[2]: #Para terminar al encontrar un codón de parada.
                    parada = True 
                    print ("-" * 132)
                    print ("La proteína resultante tiene la siguiente secuencia:", proteina)
                    print ("-" * 132)
                    break

            if parada == False:
                print ("Error. No se encontró ningún codón de parada.") 

        except Exception as ex:
            print ("!" * 132)
            print ("Error encontrado. Excepción:", ex)
            print ("!" * 132)   

print ()
input ("Pulse <INTRO> para finalizar.")
        

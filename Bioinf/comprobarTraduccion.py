print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()
print ("Bienvenido/a. Este programa comprueba que el proceso de revertir la traducción y el de la traducción funcionan correctamente.")
from random import choice #Para elegir al azar.

codigoGeneticoP = { #Creamos el diccionario. En este caso las claves son el código de una letra del aminoácido.
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'C': ['UGC', 'UGU'],
    'D': ['GAC', 'GAU'],
    'E': ['GAA', 'GAG'],
    'F': ['UUC', 'UUU'],
    'G': ['GGA', 'GGC', 'GGG', 'GGU'],
    'H': ['CAC', 'CAU'],
    'I': ['AUA', 'AUC', 'AUU'],
    'K': ['AAA', 'AAG'],
    'L': ['CUA', 'CUC', 'CUG', 'CUU', 'UUA', 'UUG'],
    'M': ['AUG'],
    'N': ['AAC', 'AAU'],
    'P': ['CCA', 'CCC', 'CCG', 'CCU'],
    'Q': ['CAA', 'CAG'],
    'R': ['AGA', 'AGG', 'CGA', 'CGC', 'CGG', 'CGU'],
    'S': ['AGC', 'AGU', 'UCA', 'UCC', 'UCG', 'UCU'],
    'T': ['ACA', 'ACC', 'ACG', 'ACU'],
    'V': ['GUA', 'GUC', 'GUG', 'GUU'],
    'W': ['UGG'],
    'Y': ['UAC', 'UAU'],
    '-': ['UAA', 'UAG', 'UGA'],
    'U': ['UGA'],
}

proteina = input ("Por favor, introduzca la secuencia de la proteína: ") 
proteina = proteina.upper ()
print ()
comprobar = list (codigoGeneticoP.keys())

for i in proteina: #Comprobar que se introduce una secuencia correspondiente a una proteína.
    if i not in comprobar:
        print ("Error. La secuencia introducida no corresponde a una proteína.")
        correct_seq = False
        break

    else:
        correct_seq = True

#Revertir la traducción:
if correct_seq == True:
    if proteina[0] != "M": #Añadir el codón de inicio si la proteína no lo incluye.
        proteina1 = "M" + proteina 
        rna = "AUG" 

    else:
        rna = ""
        proteina1 = proteina
    

    """Esto lo implementamos para cuando comparemos secuencias proteicas.
    Para simplificar, vamos a considerar que las proteínas siempre empiezan por M y que al usuario se le puede oblidar
    (aunque en algunas bacterias como E. coli se puedan utilizar GUG y UUG como codoón de inicio, pero mayoritariamente usan AUG)"""

    for i in proteina: #Revertimos la traducción:
        rna += choice (codigoGeneticoP[i])
        if i == "-":
            break

    """En este ejercicio he decidido eliminar la adición de un triplete de stop al final ya que, al añadirlo de forma aleatoria,
        luego cuando se comparen las secuencias proteicas, aunque la secuencia sea la misma, muchas veces el programa dirá que son diferentes por la aleatoriedad del codón de STOP,
            así que he decidido eliminarlo."""

    print ("-" * 132)
    print ("La secuencia de RNA es la siguiente:", rna) 
    print ("-" * 132)

if correct_seq == True:
    seguir = input ("Quieres continuar con la traducción(Y/N)?")
    seguir = seguir.upper()

else:
    seguir = "N"

#Traducción:
if seguir == "Y":
    codigoGeneticoRNA = {  #Diseñamos el diccionario que incluye el código genético.
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
    proteina2 = ""

    try:
        for i in range (0, len(rna), 3): #Para que recorra desde el codón de inicio hasta el final de 3 en 3.
            codon = rna [i:i+3]
            proteina2 += codigoGeneticoRNA[codon]
        print ("-" * 132)
        print ("La proteína resultante tiene la siguiente secuencia:", proteina2)
        print ("-" * 132)
          
    except Exception as ex:
        print ("!" * 132)
        print ("Error encontrado. Excepción:", ex)
        print ("!" * 132)   

    if proteina2 == proteina1: 
        print ("Las secuencias son iguales.")
        
    else:
        print ("Las secuencias no son iguales.")

print ()
input ("Pulse <INTRO> para finalizar.")
        

print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()
print ("Bienvenido/a. Este programa producirá una secuencia de RNA que codifique para una proteína indicada.")
from random import choice #Para elegir al azar.

codigoGenetico = { #Creamos el diccionario. En este caso las claves son el código de una letra del aminoácido.
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
    '-': ['(UAA)', '(UAG)', '(UGA)'],
    'U': ['UGA'],
}

proteina = input ("Por favor, introduzca la secuencia de la proteína: ") 
proteina = proteina.upper ()
print ()
comprobar = list (codigoGenetico.keys())

for i in proteina: #Comprobar que se introduce una secuencia correspondiente a una proteína.
    if i not in comprobar:
        print ("Error. La secuencia introducida no corresponde a una proteína.")
        correct_seq = False
        break

    else:
        correct_seq = True

if correct_seq == True:
    if proteina[0] != "M": #Añadir el codón de inicio si la proteína no lo incluye.
        rna = "AUG"

    else:
        rna = ""

    for i in proteina: #Revertimos la traducción:
        rna += choice (codigoGenetico[i])
        if i == "-":
            break

    if proteina [-1] == "-": #Esto es para asegurarse que la secuencia tendrá un codón de stop, para delimitar la secuencia de la proteína.
        print ("La secuencia de RNA es la siguiente:", rna)

    else:
        rna += choice (codigoGenetico ['-']) #He decidido añadirle un codón de parada a la secuencia para informar de que termina. Para distinguirlo, he puesto los codones de parada entre paréntesis ().
        print ("La secuencia de RNA es la siguiente:", rna)

print ()
input ("Pulse <INTRO> para finalizar.")
        
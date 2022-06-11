print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

#EJERCICIOS COLOR (PRIMERO DEL DOCUMENTO)

"""Write a program that will print only the accession names that satisfy the following criteria –
treat each criterion separately:
    contain the number 5
    contain the letter d or e
    contain the letters d and e in that order
    contain the letters d and e in that order with a single letter between them
    contain both the letters d and e in any order
    start with x or y
    start with x or y and end with e
    contain three or more digits in a row
    end with d followed by either a, r or p"""

import re

def primer_programa():
    acc_names = input ("Accession name: ") 
    criterio = re.search (("[d | e | 5]"), acc_names)
    if criterio:
        print (acc_names)
    else:
        print ("El nombre de acceso no cumple el/los criterio/s.")
    return

#print (primer_programa())

def segundo_programa():
    acc_names = input ("Accession name: ") 
    criterio = re.search (("d\we"), acc_names)
    if criterio:
        print (acc_names)
    else:
        print ("El nombre de acceso no cumple el/los criterio/s.")
    return

#print (segundo_programa())
    
def tercer_programa():
    acc_names = input ("Accession name: ") 
    criterio = re.search ("(^x | ^y)", acc_names) #REVISAR
    if criterio:
        print (acc_names)
    else:
        print ("El nombre de acceso no cumple el/los criterio/s.")
    return

#print (tercer_programa())

def cuarto_programa():
    acc_names = input ("Accession name: ") 
    criterio = re.search ("d[a | p | r]$", acc_names)
    if criterio:
        print (acc_names)
    else:
        print ("El nombre de acceso no cumple el/los criterio/s.")
    return

print (cuarto_programa())
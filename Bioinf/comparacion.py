print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()
print ("Bienvenido/a. Este programa compara dos cadenas de DNA según sus nucleótidos por posición y su longitud de secuencia.")

#Datos de entrada.
cadena1 = input("Introduzca la primera cadena de DNA: ")
cadena2 = input("Introduzca la segunda cadena de DNA: ")
cadena1 = cadena1.upper()
cadena2 = cadena2.upper()
resultado = ""
long_Cad1 = len(cadena1)
long_Cad2 = len(cadena2)

#Deisgnamos la máxima longitud y la cadena que tenga una menor longitud la rellenamos con espacios hasta igualar longitudes.
if long_Cad1 >= long_Cad2:
    max_long = long_Cad1
    cadena2 = cadena2 + (" " * (max_long - long_Cad2))

else:
    max_long = long_Cad2
    cadena1 = cadena1 + (" " * (max_long - long_Cad1))

#Variables del bucle for:
DNA1 = True
DNA2 = True
posicion = 0
print ()

for i in cadena1: #Comprobación DNA.
    if i != "A" and i != "C" and i!= "G" and i!= "T" and i!= " ":
         DNA1=False

    else: #Aquí hacemos la comparación de las dos cadenas.
        if i == cadena2[posicion]:
            resultado = resultado + "*"
        if i != cadena2[posicion]:
            if i == " " or cadena2[posicion] == " ":
                resultado = resultado + "-"    
            else:
                resultado = resultado + ":"
    posicion = posicion + 1

for i in cadena2: #Comprobación DNA.
    if i != "A" and i != "C" and i!= "G" and i!= "T" and i!= " " :
         DNA2 = False
         
if DNA1 == True and DNA2 == True:
    print("El programa muestra '*' si los nucleótidos de ambas cadenas coinciden, ':' si no coinciden y '-' cuando no se ha realizado una comparación debido a que una cadena ya ha finalizado.\n")
    print("El resultado de la comparación es el siguiente: ") 
    print(resultado)
 
else: 
    print ("Las cadenas introducidas no corresponden con DNA.")

print()
input ("Pulse <INTRO> para finalizar el programa.")
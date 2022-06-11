print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()
print("Bienvenido/a. En este programa se calculará la cadena complementaria de la cadena de ADN introducida.")

#Definimos todas las variables:
cadena = input ("Introduzca la cadena de DNA: ")
nucleotids = ["A", "T", "G" , "C"]
comprobacion = False
CADENA = cadena.upper()
cc_ntcompl = ""
cadena_inv = ""

for letter in CADENA: #Para evitar que se introduzca algo que no sea ADN.
    if letter != nucleotids[0] and letter != nucleotids[1] and letter != nucleotids[2] and letter != nucleotids[3]: 
        comprobacion = False
    else:
        comprobacion = True
     
if comprobacion == False:
    print ("Error. Introduzca DNA.")
else:
    for i in CADENA: #Copiamos la cadena complementaria en una nueva variable posición por posición.
        if i == "A":
            cc_ntcompl = cc_ntcompl + "T"
        elif i == "T":
            cc_ntcompl = cc_ntcompl + "A"
        elif i == "C":
            cc_ntcompl = cc_ntcompl + "G"
        elif i == "G":
            cc_ntcompl = cc_ntcompl + "C"
    
    for l in cc_ntcompl :
        cadena_inv = l + cadena_inv  #Copiando el iteradro antes vamos desplazando lo que copiamos de la cadena para que nos salga invertida.
    
    print ()
    print ("-" * 132)
    print ("La cadena complementaria en sentido 5' -> 3' es:", cadena_inv)
    print ("-" * 132)
input ("Pulse <INTRO> para salir.")

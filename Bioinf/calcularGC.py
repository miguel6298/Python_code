print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

#Presentación del programa y recogida de información necesaria.
print ("Bienvenido/a. En este programa se calculará el porcentaje de GC de dos secuencias de ADN e informará si las dos cadenas pertenecen a la misma especie.")
cad1 = input("Introduce la primera secuencia de DNA:")
cad2 = input("Introduce la segunda secuencia de DNA:")
print ()

cad1 = cad1.upper() #Para que no importe si el usuario introduce la cadena con letras minúsculas o mayúsculas.
cad2 = cad2.upper()

#Para asegurarse que las secuencias introducidas son de DNA.
nucleotids1 = cad1.count("A") + cad1.count("C") + cad1.count("G") + cad1.count("T")
nucleotids2 = cad2.count("A") + cad2.count("C") + cad2.count("G") + cad2.count("T")

if len(cad1) != nucleotids1 or len(cad2) != nucleotids2:
    print("Error, esto no es DNA. Introduce una cadena de DNA.")

else:
    GC1 = float ((cad1.count("G")+cad1.count("C")) / len(cad1))*100 #Contar cantidades relativas de G y C en cada cadena.
    GC2 = float ((cad2.count("G")+cad2.count("C")) / len(cad2))*100
 
    diferencia = abs (GC1-GC2) 

    print ("El contenido en GC de la primera secuencia es:", GC1, "%")
    print ("El contenido en GC de la segunda secuencia es:", GC2, "%")
    print ()

    if diferencia <= 2.5: #Para comprobar si son de la misma especie.
        print ("Las dos secuencias de DNA pertenecen a la misma especie. La diferencia de %GC entra ambas secuencias es del", diferencia, "%")

    else: 
        print ("Las dos secuencias de DNA pertencen a especies distintas. La diferencia de %GC entra ambas secuencias es del", diferencia, "%")

print ()    
input ("Presione <INTRO para finalizar.")


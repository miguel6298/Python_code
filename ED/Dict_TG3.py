import string 
import os 

    
    
def Recorrer_fichero (fichero): 
    glosario = {}
    contador = [0]

    for line in fichero:
        
        contador[0] += 1
        line = line.strip()
        line.replace(string.punctuation, ' ')
        palabras = line.split()
        
        
        for palabra in palabras:           
            long = len(palabra)
            if long >= 4:
                if palabra not in glosario.keys():
                    glosario[palabra] = [contador]
                else:
                    glosario[palabra].append(contador)

        return glosario
    
def Crear_Glosario (fichero, glosario): 
    nombre = input ("Introduce el nombre del nuevo archivo (sin añadir la extensión): ")
    output_file = open(nombre + ".glo.txt", "a")
    for i in glosario.keys():
        x = glosario[i]
        output_file.write(i)
        for numero in x:
            numerodef = str (numero)
            output_file.write('\t' + numerodef)
        output_file.write ('\n')

    print(glosario)
    output_file.close()
    fichero.close()

   
def main():
    ruta = input ("Introduce la ruta en el que se encuentra el fichero:")
    nombre = input ("Ahora, introduce el nombre del archivo: ")

    try: 
        os.chdir(ruta)
        fichero = open (nombre, "r")
    except:
        print ("ERROR. Revise la ruta y el nombre del fichero introducidos.")

    glosario = Recorrer_fichero (fichero)
    Crear_Glosario (fichero, glosario)

if __name__ == '__main__':
    main()

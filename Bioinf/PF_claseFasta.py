##################################
#                                #
#   Autor : Miguel Ruiz Ibáñez   #
#                                #
##################################


import os
import sys
import numpy as np
from matplotlib import pyplot as plt
import re


def comprobar (path, name): 
    """
    Función para comprobar que un fichero está en formato fasta.
    
    Returns:
    --------
    bool:
        Si es un fichero fasta, devuelve True
        
        Si no es un fichero fasta, devuelve False
    """
    
    os.chdir(path) 
    f1 = open(name, "r")
    line = f1.readline()

    if line.startswith(">"):
        f1.close()
        return True
    else:
        f1.close()
        return False


class Fasta:
    """
    Clase para trabajar con ficheros fasta (.fa).
    """

    def __init__(self, path, name):
        """
        Constructor donde se definen los atributos de la clase.
        """
        
        self.path = path
        self.name = name 
        comprobar(self.path, self.name)
        if comprobar(self.path, self.name) == False:
            raise TypeError ("El archivo introducido no está en formato fasta (.fa). \
                             Revise el archivo y vuelve a intentarlo más tarde.")
        else:
            self.sec_limpia = self.obtenersec()
               
    def obtenersec(self):
        """
        Método que lee un fichero y limpia la secuencia eliminando la cabecera y
        los caracteres invisibles, guardándola en una variable de clase.
        
        Returns:
        --------
        cadena : (str) Devuelve una variable str que contiene la secuencia limpia del fichero.
        """
        os.chdir(self.path) 
        lista=[]
        archivo = open(self.name, 'r')
 
        for line in archivo:
            if '>' in line:
                continue
            else:
                linea=line.strip("\n")
                lista.append(linea)

        cadena = ''.join(lista)
        archivo.close()
        cadena = cadena.upper()
        return cadena

    def dotPlot(self, secuencia = "misma"):
        """
        Método para dibujar un dot plot que compara dos secuencias. Si no se indica ninguna otra
        secuencia, se usara la misma por defecto.
        
        Returns:
        --------
        plt.show() : (plot) Devuelve un gráfico de la matriz de coincidencias de las dos secuencias.
        """
        
        secuencia1 = self.sec_limpia
        
        if secuencia != "misma":
            if comprobar(self.path, secuencia) == False:
                print ("El archivo introducido no está en formato fasta (.fa). Revise el archivo y vuelve a intentarlo más tarde.")
                sys.exit(1)
            
            else:
                lista2 = []
                sec2 = open(secuencia, "r")
                for line in sec2:
                    if '>' in line:
                        continue
                    else:
                        linea = line.strip("\n")
                        lista2.append(linea)
                        cadena2 = ''.join(lista2)
                        
                secuencia2 = cadena2
                sec2.close()
           
                if len(secuencia1) > 1000:
                    secuencia1=secuencia1[:999] #Para evitar un error de memoria 
                        
                if len(secuencia2) > 1000:
                    secuencia2=secuencia2[:999]
                        
                if len(secuencia1) <= len(secuencia2):
                    rangoSec = len(secuencia1)
                else:
                    rangoSec = len(secuencia2)
        
                matriz = np.zeros([rangoSec, rangoSec])   
                for x in range (rangoSec):
                    for i in range (rangoSec):
                        if secuencia1[x] == secuencia2[i]:
                            matriz[x,i] = 1
                                
                plt.matshow(matriz, cmap='Greys')
                plt.title('Dot plot')
                plt.xlabel(self.name) 
                plt.ylabel(secuencia)
                """
                El nombre de los ejes es intercambiable ya que estamos representando
                una matriz de coincidencias (0 y 1), pero lo indico así para que se sepan 
                los ficheros que se están comparando.
                """
                return plt.show()
            
        else:
            secuencia2 = secuencia1
            
            if len(secuencia1) > 1000:
                secuencia1 = secuencia1[:999] #Para evitar un error de memoria 
                secuencia2 = secuencia2[:999]       
                
            matriz = np.zeros([(len(secuencia1)), len(secuencia2)])         
            for x in range (len(secuencia1)):
                for i in range (len(secuencia2)):
                    if secuencia1[x]== secuencia2[i]:
                        matriz[x,i] = 1
                                
            plt.matshow(matriz, cmap='Greys')
            plt.title('Dot plot')
            plt.xlabel(self.name)
            plt.ylabel(self.name)
            return plt.show()


    def longSec(self):
        """
        Método para calcular la longitud de la secuencia.
        
        Returns:
        --------
        len (self.sec_limpia) : (int) Devuelve la longitud de la secuencia self.
        """
        
        print ("\t-La longitud de la secuencia es de", len(self.sec_limpia), "nucleótidos.")
    

    def tripletes2int(self):
        """
        Método para traducir los tripletes a enteros.
        
        Returns:
        --------
        lista_tripletes : (list) Devuelve una lista de enteros con la traducción de los
        tripletes de la secuencia self a enteros.
        """
        nucleotidos = "ACGT"
        lista_tripletes = []
        lista = []
        d = {}
        valor = 0

        for letter1 in nucleotidos:
            for letter2 in nucleotidos:
                for letter3 in nucleotidos:
                    codon = letter1 + letter2 + letter3
                    lista.append (codon)
        
        for elemento in lista:
            d[elemento] = valor
            valor += 1
        
        for i in range (0, len(self.sec_limpia), 3):
            if self.sec_limpia[i:i+3] in d:
                triplete = self.sec_limpia[i:i+3]
                lista_tripletes.append(d[triplete])
            
        return lista_tripletes

    def cadCompl(self):
        """
        Método para construir la cadena complementaria a la secuencia self.
        
        Returns:
        --------
        cadena_inv : (str) Cadena con la secuencia complementaria a la secuencia self.
        
        """
        
        cc_ntcompl = ""
        cadena_inv = ""
        
        for i in self.sec_limpia:
            if i == "A":
                cc_ntcompl = cc_ntcompl + "T"
            elif i == "T":
                cc_ntcompl = cc_ntcompl + "A"
            elif i == "C":
                cc_ntcompl = cc_ntcompl + "G"
            elif i == "G":
                cc_ntcompl = cc_ntcompl + "C"
            elif i == "N":
                cc_ntcompl = cc_ntcompl + "N"
    
        for l in cc_ntcompl :
            cadena_inv = l + cadena_inv  #Copiando el iterador antes vamos desplazando, para invertir la secuencia. 
    
        return cadena_inv
    
    def GpC(self):
        """
        Método para calcular el contenido de GC de la secuencia self. Una secuencia rica es GC puede indicar 
        la presencia de abundantes promotores en mamíferos.
        
        Returns:
        --------
        contenido_GC : (float) Devuelve el porcentaje de GC de la secuencia self.
        
        """
        
        contenido_GC = float ((self.sec_limpia.count("G") + self.sec_limpia.count("C")) / len(self.sec_limpia)) * 100
        contenido_GC = "{:.2f}".format(contenido_GC)
        print ("El porcentaje de GC de la secuencia es del", contenido_GC, "%.")
        
    
    def seqSearcher(self, seq):
        """
        Método para buscar una secuencia indicada por el usuario en la secuencia self.
        
        Returns:
        --------
        Si se encuentra la secuencia buscada en la secuencia self:
            (i, i + l) : (tupla) Devuelve una tupla (vector) de la(s) posición(es)
            donde se encuentra la secuencia buscada en la secuencia self.
        
        Si no se encuentra la secuencia buscada:
            str : "Secuencia no encontrada."
        
        """
        sequence = ""
        contador = 0
        l = len(seq)
        
        for i in range (0, len(self.sec_limpia)):
            sequence = self.sec_limpia[i:i+l]
            if sequence == seq:
                contador += 1
                print ("-La secuencia buscada se encuentra entre las posiciones %d y %d" % (i, i + l))
                
        if contador == 0:
            print ("-Secuencia no encontrada.")  
            

    def frecTripletes(self): 
        """
        Método para calcular la frecuencia absoluta de los tripletes de la secuencia self,
        considerando la pauta de lectura desde el inicio de la secuencia.
        
        Returns:
        --------
        d : (dict) Devuelve un diccionario con la frecuencia absoluta de cada triplete.
        
        plt.show() : (plot) Devuelve un barplot con las frecuencias de los tripletes.
                            En el barplot se muestran los datos en el mismo orden que se muestran
                            en el diccionario.
        """
        
        nucleotidos = "ACGT"
        lista = []
        d = {}
        valor = 0
        dicList = []

        for letter1 in nucleotidos:
            for letter2 in nucleotidos:
                for letter3 in nucleotidos:
                    codon = letter1 + letter2 + letter3
                    lista.append (codon)
        
        for elemento in lista:
            d[elemento] = valor
        
        for nt in range (0, len(self.sec_limpia), 3):
            if self.sec_limpia[nt:nt+3] in d:
                d[self.sec_limpia[nt:nt+3]] += 1
        
        print ("La frecuencia absoluta de cada triplete es:\n", d)
    
        for i in list(d.keys()):
            if i == "AAA" or i == "CCC" or i == "GGG" or i == "TTT":
                dicList.append(i)
            else:
                dicList.append("")
        
        plt.bar(range(len(d)), list(d.values()), align='center')
        plt.xticks(range(len(d)), dicList)
        plt.title("Frecuencia absoluta tripletes")
        plt.xlabel("Tripletes")
        plt.ylabel("Frecuencia")
        
        plt.savefig("MRuiz.barplot.png")
        
        return plt.show()
    
    
    def transcribe(self):
        """
        Método para transcribir la secuencia self de ADN a ARN.
        
        Returns:
        --------
        cad_ARN : (str) Devuelve una cadena con la secuencia transcrita.
        """
        
        cad_ARN = ""
        
        for i in self.sec_limpia:
            if i == "A":
                cad_ARN = cad_ARN + "U"
            elif i == "T":
                cad_ARN = cad_ARN + "A"
            elif i == "C":
                cad_ARN = cad_ARN + "G"
            elif i == "G":
                cad_ARN = cad_ARN + "C"
            elif i == "N":
                cad_ARN = cad_ARN + "N"
    
        return cad_ARN
    
    
    def robustez(self):
        """
        Método para calcular el porcentaje de nucleótidos identificados.
        
        Returns:
        --------
        nt_especificados : (float) Devuelve el porcentaje de nucleótidos identificados.
        """
        
        nt_especificados = (1- (self.sec_limpia.count("N") / len(self.sec_limpia))) * 100
      
        print ("-La robustez de la secuenciación es del", nt_especificados, "%.")
        
    
    def buscarORF(self):
        """
        Método para buscar ORF (Open Reading Frames) en la secuencia self.
        
        Returns:
        --------
        Si se encuentra alguna ORF:
            listaORF : (list) Devuelve una lista que contiene las ORF de la secuencia self.
            
        Si no se encuentra ninguna ORF:
            str : Devuelve una cadena que indica que no se ha encontrado
            ninguna ORF en la secuencia self.
        """

        ORF = self.sec_limpia
        codones_stop = ["TAG", "TAA", "TGA"]
        codon_inicio = "ATG"
        inicio = ORF.find(codon_inicio)
        listaORF = []
     
        if inicio != None:
            
            for nt in range (inicio, len(ORF), 3):  
                if ORF[nt:nt+3] in codones_stop:
                    secORF = ORF[inicio:nt+3]
                    listaORF.append(secORF) 
                    ORF = ORF[nt+3:]
                    inicio = ORF.find(codon_inicio)
                    
            print ("Las ORFs de la secuencia del fichero", self.name, "es/son:\n", listaORF)
        
        else:
            print ("No se ha encontrado nignuna ORF.")
        
    
    def virus(self):
        """
        Método para buscar una secuencia patrón de un virus en la secuencia self.
        
        Returns:
        --------
        Si encuentra la secuencia patrón del virus:
            lSecVirus : (list) Devuelve una lista con las posiciones (inicio y final)
            donde se ha encontrado el patrón viral en la secuencia self. 
            
        Si no encuentra la secuencia:
            str : Devuelve una cadena indicando que no se ha encontrado el patrón en la secuencia self.
        """
        
        lSecVirus = []
        pattern = re.compile('((AG){1,}(CAGATA|AGATA)([ATCG]+?)(GAT){2,3})')
        virusp = pattern.finditer(self.sec_limpia)
        
        for nt in virusp:
            lSecVirus.append(nt.span())
            
        if len(lSecVirus) != 0:
            print ("Las posiciones en las que se ha encontrado la secuencia patrón del virus son:\n")
            print (lSecVirus)
            
        else:
            print ("-La secuencia del virus no se ha encontrado en %s." % (self.name)) 
             
        
    def grabaFa(self, nomFich):
        """
        Método para grabar el contenido del fichero de entrada en otro fichero
        con el nombre que el usuario indica. 
        
        Returns:
        --------
        fichero_nuevo : (file) Devuelve un fichero con el nombre elegido por el usuario,
                               conteniendo la información del fichero de entrada.
        """
    
        nombre = nomFich + ".fa"
        f = open(self.name, "r")
        fichero_nuevo = open (nombre, "w")

        for line in f.readlines():
            fichero_nuevo.write(line)
        
        f.close()
        fichero_nuevo.close()
        print ("\t-El fichero %s se ha grabado en %s con el nombre %s." %(self.name, self.path, nombre))


def main():
    print ("-" * 85)
    print ("| Bienvenido/a. En este programa comprobaremos el funcionamiento de la clase Fasta. |")
    print ("-" * 85)
    print()
    print ("¡AVISO!: Se han dejado las llamadas a los métodos como comentarios\
por si se quieren utilizar para la comprobación y corrección.")

    ruta = input ("Introduce la ruta donde se encuentra el fichero: ")
    archivo = input ("A continuación, introduce el nombre del archivo fasta: ")
    fich = Fasta(ruta, archivo)
    print ()
    
    #print (fich.sec_limpia)
    #fich.grabaFa("prueba")
    #fich.longSec()
    #print (fich.tripletes2int())
    #print (fich.cadCompl())
    #fich.GpC()
    #fich.seqSearcher("CAGATA")
    #print (fich.transcribe())
    #fich.robustez()
    #fich.frecTripletes()
    #fich.buscarORF()
    #fich.virus()
    #fich.dotPlot()
    
    
    print ()
    input ("Pulse <INTRO> para finalizar.")

if __name__ == '__main__':
    main()
 

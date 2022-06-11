# -*- coding: utf-8 -*-
"""
Este programa crea la clase Registro, que se compone de la posición de inicio 
en la que mapea una secuencia, la calidad del mapeo y la longitud de la 
secuencia que ha sido mapeada. Además, hay una serie de funciones que nos
permiten leer un fichero SAM, cuantificar el número de mapeos frente a una 
base de la secuencia de referencia y escribirlo en un fichero. Por último,
otra función permite generar una gráfica del número de reads en cada posición.  

"""
import re
import numpy as np
import matplotlib.pyplot as plt

class Registro:
    """
    La clase registro tiene tres atributos: la posición de inicio en la que 
    mapea una secuencia, la calidad del mapeo y la longitud de la secuencia
    mapeada. Estos atributos se añaden a un objeto de la clase registro
    mediante un método.
    """
    
    def __doc__():
        """
        Mediante este método podremos explicar para que sirven cada una de las
        funciones o los métodos expuestos. 
        """
        
        pass
    
    def __init__(self):
        """
        Constructor por defecto. Inicia un objeto a la clase registro mostrando
        los tres atributos que tiene la clase y diciendo que son enteros.
        """
        
        self.inicio = int()
        self.calidad = int()
        self.longitud = int()
        
    def analizar_linea(self, linea):
        """
        Método mediante el cual se pasa una linea y se introduce cada dato
        como atributo del objeto de la clase registro.
        
        Args:
            linea (str) Linea de un fichero de la que se extraerán los
            diferentes atributos.
        """

        datos = linea.split("\t")
        self.inicio = int(datos[3])
        self.calidad = int(datos[4])
        self.longitud = len(datos[9])
            
    def __str__(self):
        """
        Devuelve una representación en forma de cadena de la instancia.

        Returns:
            Cadena que se visualiza cuando se imprime la instancia.
        """
        
        return "%d\t%d\t%d"%(self.inicio, self.calidad, self.longitud)
    
def leer_fichero(fichero):
    """
    Esta función nos permite leer un fichero SAM. A partir de este fichero 
    podemos conocer la longitud de la secuencia de referencia y cada una de las 
    variables que componen la clase registro. La longitud de la secuencia de
    referencia se ha extraido gracias a expresiones regulares del fichero SAM.
    Para las líneas con información de reads se crea un nuevo objeto, se
    utiliza el método de añadir atributos y se incluye en una lista dicho
    objeto.
    
    Args: 
        fichero (file) fichero SAM en el que se encuentra toda la información 
        a extraer. 
        
    Returns: 
        longitud_genoma (int) Número entero que indica cuánto mide el genoma
        de referencia.
        
        lista_registros (lista) lista con todos los objetos de la clase
        Registro analizados.
    """
    
    lista_registros = []
    file = open(fichero, "r")
    patron = re.compile("LN:(\d+)")
    
    for linea in file:
        if linea[0] == "@":
            if patron.search(linea):
                longitud_genoma = int(patron.search(linea).group(1))
        else:
            f = Registro()
            f.analizar_linea(linea)
            lista_registros.append(f)
            
    return (longitud_genoma, lista_registros)

def cubrimiento(longitud_genoma, lista_registros):
    """
    Con esta función realizamos una cuantificación de las bases que mapean 
    contra cada base del genoma de referencia. Primero se hace una lista de
    contadores mediante una lista por comprensión y después por cada posición
    que se encuentre dentro de un read se suma una al contador de esa posición.
    
    Args: 
        longitud_genoma (int) Entero que nos indica la longitud del genoma de
        referencia
        
        lista_registros (lista) Lista con cada uno de los objetos que
        corresponden a cada read.
    
    Return: 
        contadores (lista) Nos devuelve una lista en la que cada posición
        contiene el  número de veces que hay mapeada una base del genoma de 
        referencia. 
    """
    
    contadores = [0 for i in range(longitud_genoma)]
    
    for objeto in lista_registros:
        if objeto.calidad == 60:
            for posicion in range(objeto.longitud):
                contadores[objeto.inicio+posicion-1] += 1
                
    return contadores

def escribir_fichero(fichero, longitud_genoma, contadores):
    """
    Nos permite escribir en un nuevo fichero (que tenga el mismo nombre que el
    fichero SAM original) todas las posiciones del genoma de referencia y
    la cuantificación hecha en la función anterior para cada posición. 
    
    Args: 
        fichero (file) Nos servirá para obtener el nombre del fichero
        introducido y, mediante expresiones regulares, quedarnos solo con
        el nombre sin la extensión.
        
        longitud_genoma (int) Entero que nos indica la longitud del genoma de
        referencia.
        
        contadores (lista) Lista en la que cada posición contiene el  número 
        de veces que hay mapeada una base del genoma de referencia. 
    """
    
    nombre_archivo = re.compile("(.+)\..+")
    nombre_sin_extension = nombre_archivo.search(fichero).group(1)
    
    file = open(nombre_sin_extension + ".cub", "w")
    indices = [str(1+i) for i in range(longitud_genoma)]
    
    for indice in range(len(indices)):
        file.write("%s: %s\n"%(indices[indice], contadores[indice]))
        
    file.close()

def dibujar_grafica(longitud_genoma, contadores):
    """
    Función que permite dibujar una gráfica en la que se representa en el
    eje X cada una de las posiciones del genoma de referencia y en el eje Y
    el número de reads en dicha posición.
    
    Args:
        longitud_genoma (int) Entero que nos indica la longitud del genoma de
        referencia. para poder generar el eje X.
        
        contadores (lista) Lista que nos indica el número de reads en cada
        posición.
    """
    
    x = np.array([(1+i) for i in range(longitud_genoma)])
    y = np.array(contadores)
    plt.plot(x, y, linewidth = 0.5)
    
    plt.xlabel("Posición en el genoma")
    plt.ylabel("Número de reads")
    plt.title("Numero de reads por posición en el genoma")
    
    plt.figure(figsize=(16, 2), dpi=160) #Para hacer el gráfico más grande
    plt.show()
    
def main():
    #Pedimos al usuario el nombre del fichero SAM. 
    fichero = input("Dime el nombre del fichero SAM: ")
    
    #Leemos el fichero y extraemos la información necesaria. 
    longitud, lista = leer_fichero(fichero)
    
    #Realizamos la cuantificación. 
    contadores = cubrimiento(longitud, lista)
    
    #Guardamos el resultado en un nuevo fichero. 
    escribir_fichero(fichero, longitud, contadores)
    
    #Construimos la gráfica que nos permite ver los reultados. 
    dibujar_grafica(longitud, contadores)

if __name__== "__main__":
    main()
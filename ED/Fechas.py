#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#############################
#                           #
#   ~ Miguel Ruiz Ibáñez ~  #
#                           #
#############################

"""
Construcción de la clase Fecha y ordenación de un fichero de fechas.

"""

import os 

class Fecha: 
    """
    Clase para trabajar con fechas. Todas las fechas se componen por día, mes 
    y año, que son los tres atributos que indicamos en el constructor. 
    """
    year = 1583
    month = 1 
    day = 1
    
    def __init__(self, day, month, year):
        """
        Designar atributos

        Returns
        ------
        None
        """

        self.year = year
        self.month = month
        self.day = day
        
    def __str__ (self):
        """
        Devuelve una representación en forma de cadena de la instancia. 
        
        Returns: 
            str Cadena que se visualiza al imprimir la instancia. 
        """
        fecha_str = str(self.day) + '/' + str(self.month) + '/' + str(self.year)
        return fecha_str
    
    def __gt__ (self, otra_fecha): 
        """
        Permite comparar fechas. 
        
        Args: 
            Otra_fecha (Fecha). Instancia de la clase. 
        
        Returns: 
            Nos devuelve un booleano que será True cuando una fecha sea 
            mayor que otra y False cuando no lo sea. 
        """
        if self.year > otra_fecha.year: 
            return True
        elif self.year == otra_fecha.year: 
            if self.month > otra_fecha.month:
                return True
            elif self.month == otra_fecha.month:
                if self.day > otra_fecha.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        
    def __eq__ (self, otra_fecha):
        """
        Permite comprobar si una fecha es igual que otra. 
            
        Args: 
            Otra_fecha (Fecha). Instancia de la clase.
                
        Returns: 
        Nos devuelve un booleano que será True cuando una fecha sea 
            igual que otra y False cuando sean distintas.  
        """
            
        if self.year == otra_fecha.year:
            if self.month == otra_fecha.month:
                if self.day == otra_fecha.day:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
        

def main(): 

    #Explicar la función del programa. 
    print ("Este programa ordena fechas en valor ascendente.")
    print ()
    
    #Pedir el nombre del archivo y lo abrirlo en modo lectura. 
    nombre = input("Introduzca el nombre del fichero: ")
    
    fichero = open (nombre, "r")
    
    #Crear tantas instancias de la clase Fecha como fechas hay en el archivo. 
    
    fechas = fichero.readlines()
    lista_fechas = []
    
    #Asignar los atributos de la clase Fecha a cada una de las fechas. 
    for i in fechas: 
        entrada = i.split("/")
        fecha = Fecha(int(entrada[0]), int(entrada[1]), int(entrada[2]))
        #Introducir estas instancias en una nueva lista que contenga las fechas. 
        lista_fechas.append(fecha)
        #Ordenar la lista en orden ascendente. 
        lista_fechas.sort()
        
    #Abrir un fichero vacío en el que escribir las fechas ordenadas.      
    salida = open ("orden" + nombre, "w")
    for x in lista_fechas:
                salida.write (x.__str__() + '\n')
    salida.close()

if __name__ == "__main__":
    main ()

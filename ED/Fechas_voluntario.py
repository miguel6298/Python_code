#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este programa crea la clase Fecha y algunas funciones útiles que nos permiten 
ordenar las fechas que hay en un archivo. 

"""

import os 

class Fecha: 
    """
    Clase para trabajar con fechas. Todas fechas se componen por día, mes 
    y año, que son las tres variables que indicamos en el constructor. 
    """
    año = 1583
    mes = 1 
    dia = 1
    
    def __init__(self, dia, mes, año):
        """
        Constructor por defecto. 
        """
        self.año = año
        self.mes = mes
        self.dia = dia
        
    def __str__ (self): 
        """
        Devuelve una representación en forma de cadena de la instancia. 
        
        Return: 
            str Cadena que se visualiza al imprimir la instancia. 
        """
        fecha_str=str(self.dia)+'/'+str(self.mes)+'/'+str(self.año)
        return fecha_str
    
    def __gt__ (self, otra_fecha): 
        """
        Permite la comparación entre fechas. 
        
        Args: 
            Otra_fecfa (Fecha). Instancia de la clase. 
        
        Return: 
            Nos devuelve un booleano que será True cuando una fecha sea 
            mayor que otra y false cuando esta comparación no sea así. 
        """
        if self.año > otra_fecha.año: 
            return True
        elif self.año == otra_fecha.año: 
            if self.mes>otra_fecha.mes:
                return True
            elif self.mes==otra_fecha.mes:
                if self.dia>otra_fecha.dia:
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
                Otra_fecfa (Fecha). Instancia de la clase.
                
            Return: 
                 Nos devuelve un booleano que será True cuando una fecha sea 
                 igual que otra y false cuando las fechas son distintas.  
            """
            
            if self.año==otra_fecha.año:
                if self.mes==otra_fecha.mes:
                    if self.dia==otra_fecha.dia:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        

def main(): 
    #Le explicamos al usuario lo que hace el proggrama. 
    print ("Este programa ordena fechas en valor ascendente.")
    
    #Pedimos al usuario el nombre del archivo y lo abrimos en modo lectura. 
    nombre = input("Dime el nombre del fichero")
    
    file = open (nombre, "r")
    
    #creamos tantas instancias de la clase Fecha como fechas hay en el archivo. 
    
    fechas = file.readlines()
    lista_fechas = []
    
    #asignamos los atributos de la clase fecha a cada una de las fechas. 
    for i in fechas: 
        entrada = i.split(" ")
        fecha = Fecha(int(entrada[2]),int(entrada[1]),int(entrada[0]))
        #Introducimos estas instancias en una nueva lista que tiene las fechas. 
        lista_fechas.append(fecha)
        #Ordenamos esta lista en orden ascendente. 
        lista_fechas.sort()
        
    #Abrimos un fichero vacío en el que escribiremos las fechas ordenadas.      
    solucion = open ("ordenado" + nombre, "a")
    for x in lista_fechas:
                solucion.write(x.__str__()+'\n')
    resultado.close()
    
    
if __name__ == "__main__":
    main ()

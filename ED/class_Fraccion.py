# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 19:06:26 2020

@author: plope
"""

#Grupo Eds_Gr04
#Creación de la clase Fraccion
import math


class Fraccion:

    def __init__(self, numerador, denominador):
        self.numerador=int(numerador)
        self.denominador=int(denominador)
        self.mcd()
    def leer(self):
        numerador=self.numerador
        denominador=self.denominador

        if denominador == 0:
            raise ZeroDivisionError ("El denominador de la fracción no puede ser cero.")
        else:
            self.numerador = numerador
            self.denominador = denominador
        
       
    def __str__(self):
        '''
        Permite la visualizacion en forma de cadena
        '''
        
        return str(self.numerador) + "/" + str(self.denominador)
    

    def __add__(self, otraF):
        '''
        Se utiliza para las operaciones aritméticas "+"
        
        Parameters
        ----------
        otraF : Racional.

        Returns
        -------
        resultado : Racional. Resultado de la suma. 

        '''
        if self.denominador==otraF.denominador:
            num=self.numerador+otraF.numerador
            den=self.denominador
        else:
            num = self.numerador * otraF.denominador + otraF.numerador * self.denominador
            den = self.denominador * otraF.denominador
            
        div = self.mcd()
        resultado = Fraccion (num/div, den/div)
        return resultado
    
    def __sub__(self, otraF):
        '''
        Se utiliza para las operaciones aritméticas "-"

        Parameters
        ----------
        otraF : Racional

        Returns
        -------
        resultado : Racional. Resultado de la resta. 

        '''
        if self.denominador==otraF.denominador:
            num=self.numerador-otraF.numerador
            den=self.denominador
        else:
            num = self.numerador * otraF.denominador - otraF.numerador * self.denominador
            den = self.denominador * otraF.denominador
        div = self.mcd()
        resultado = Fraccion (num/div, den/div)
        return resultado
    
    def __mul__(self, otraF):
        '''
        Parameters
        ----------
        otraF :Racional

        Returns
        -------
        resultado : Racional. Resultado de la multiplicacion.

        '''
        num=self.numerador*otraF.numerador
        den=self.denominador*otraF.denominador
        
        div = self.mcd()
        resultado = Fraccion (num/div, den/div)
        return resultado
        
    def __div__(self,otraF):
        num=self.numerador*otraF.denominador
        den=self.denominador*otraF.numerador
        
        div = self.mcd()
        resultado = Fraccion (num/div, den/div)
        return resultado
        
        
    def evaluar (self): 
        '''
        Realiza la división entre numerador y denominador. 

        Returns
        -------
        division : float
            Resultado obtenido tras realizar el cociente.

         '''   
        division = self.numerador / self.denominador
        return (division) 
    
    def mcd(self):
        '''
        Maximo Común Divisor de dos números, a y b. 

        Argumentos:
            a(int)
            b(int)

        Return:
        MCD: int
        '''
        num1 = self.denominador
        num2 = self.numerador
        
        #Seleccionamos el mayor y el menor de las variables a y b, respectivamente
        a=max(num1,num2)
        b=min(num1,num2)

        #Mientras el resto de la division sea mayor que 0, el resto de la division sera el dividendo entre el divisor
        resto = 0
        while (b > 0):   
            resto = b     
            b = a % b
            a = resto
        return a
    
    def mcm(self):
        #El MCM de a y b puede calcularse con el algoritmo: mcm=(a*b)/mcd
    
        #Seleccionamos el mayor y el menor de las variables a y b, respectivamente
        
        num1 = self.numerador
        num2 = self.denominador
        
        a=max(num1,num2)
        b=min(num1,num2)

        while b:
            mcd = b
            b = a % b
            a = mcd
            mcm=(num1*num2//mcd)
        return mcm
    
def main():
    print("Introduzca el nº de elementos a sumar:")
    n=int(input("\t"))
    
    if n<=0 or n>164:
        print("Error")
        print("\t El número introducido no puede ser menor o igual a 0. Tampoco puede ser mayor que 165.")
    else:
      f1=Fraccion(1,math.factorial(0))
      f2=Fraccion(1,math.factorial(1))
      
      
      for i in range(1,n):
              f2.numerador=1
              f2.denominador=math.factorial(i)
              
              f1+=f2
    
    print("El valor estimado de e es: ",f1) 
    print("En forma de cociente: ", f1.evaluar())
    
if __name__ == "__main__":
    main()    

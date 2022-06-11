#Grupo Eds_Gr04
#Creación de la clase Fraccion

class Fraccion:

    def gdc (self, a, b):
        while a % b != 0:
            aAnterior = a
            bAnterior = b
            a = bAnterior
            b = aAnterior % bAnterior
            return (a)

    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ZeroDivisionError ("El denominador de la fracción no puede ser cero.")
        else:
            self.numerador = numerador
            self.denominador = denominador
    
    def __str__ (self): 
        mostrar = (str (self.numerador) + '/' + str (self.denominador))
        print (mostrar)

    def __add__(self, otraF):
         nuevoNum = self.numerador * otraF.denominador + self.denominador * otraF.numerador
         nuevoDen = self.denominador * otraF.denominador
         comun = gdc (nuevoNum, nuevoDen)
         return Fraccion(nuevoNum/comun, nuevoDen/comun)

    def _evaluar (self): 
        division = self.numerador / self.denominador
        return (division) 

f1 = Fraccion (2,2)
f2 = Fraccion (5,4)
print (f1 + f2)
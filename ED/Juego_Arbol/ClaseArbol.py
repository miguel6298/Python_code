
class Arbol:
    def __init__(self, raiz: int = None, izdo : Arbol = None, dcho : Arbol = None): #Ojo, el rpopio tipo no se puede utilizar como tipo, entonces se pone como comentario, el problema es que entonces el None da problemas, sería poner algo como izdo=None, #: Arbol
        self.vacio = bool ()
        #self.info = ??? #No sé el tipo porque podemos poner cualquier tipo de dato. Poner int cuando ? porque con ? nos dará problemas.
        self.izdo = Arbol()
        self.dcho = Arbol()

        if raiz == None:
            self.vacio = True
        else:
            self.info = raiz
        
        if izdo == None:
            self.izdo = True
        else:
            self.izdo = izdo
        
        if dcho == None:
            self.dcho = True
        else:
            self.dcho = dcho

#Todo esto lo haremos automático en adelante, ahora esto es para explicarlo bien.
arb1 = Arbol()
arb2 = Arbol(1)
arb3 = Arbol(2) 


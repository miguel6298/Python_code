

class Cola: #Esto es un copypaste de la clase Pila, así que puede haber cosas mal.

    def __init__(self):
        """
        Iniciar lista vacía

        Returns
        ------
        None
        """

        self.elementos = []

    def Encolar(self, x : str):  #Porque vamos a añadir A, B y C, por eso ponemos que será str.
        """
        Pone en la cima el elemento pasado como parámetro
        Parameters
        -----------
        x : str
            El elemento a apilar

        Returns
        ------
        None
        """
        self.elementos.append(x)
        return
    
    def Desencolar(self) -> bool: #Solo se debería poder desapilar si hay elementos en la pila, por tanto, aquí tb se diría si está vacía o no.
        """
        Eliinar el último elemento de la pila y devuelve true si lo ha conseguido y false si no.

        Returns
        -------
        bool
            True si se ha podido
            False si no se ha podido
        """
        if self.elementos:
           self.elementos.pop ()
           ok = True
        
        else:
            ok = False
        
        return ok

    def ColaVacia(self):
        """
        Determina si la pila tiene o no elementos

        Returns
        -------
        bool
            True si está vacía
            False si no lo está
        """
        return not self.elementos
    
    def PrimerCola(self) -> (bool, str): #Hay que poner los paréntesis importante
        """
        Devuelve el elemento de la cima si lo hay.
        
        Returns
        -------
        bool,str
            Si hay o no elementos
            El elemento de la cima
        """
        if self.ColaVacia():
            return False
        else:
            return True, self.elementos[0]

def main():

    cola = Cola()
    cola.Encolar("A")
    cola.Encolar("B")
    cola.Encolar("C")

    print (cola.PrimerCola()[1])

    cola.Encolar("D")
    print (cola.PrimerCola()[1])

    cola.Desencolar()
    cola.Desencolar()

    print(cola.PrimerCola()[1])

    cola.Encolar("E")
    cola.Encolar("F")

    while not cola.ColaVacia():
        print(cola.PrimerCola()[1])
        cola.Desencolar()

if __name__ == "__main__":
    main ()

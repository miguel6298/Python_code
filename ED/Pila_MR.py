

class Pila:

    def __init__(self):
        """
        Iniciar lista vacía

        Returns
        ------
        None
        """

        self.elementos = []

    def Apilar(self, x : str):  #Porque vamos a añadir A, B y C, por eso ponemos que será str.
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
    
    def Desapilar(self) -> bool: #Solo se debería poder desapilar si hay elementos en la pila, por tanto, aquí tb se diría si está vacía o no.
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

    def PilaVacia(self):
        """
        Determina si la pila tiene o no elementos

        Returns
        -------
        bool
            True si está vacía
            False si no lo está
        """
        return not self.elementos
    
    def CimaPila(self) -> (bool, str): #Hay que poner los paréntesis importante
        """
        Devuelve el elemento de la cima si lo hay.
        
        Returns
        -------
        bool,str
            Si hay o no elementos
            El elemento de la cima
        """
        if self.PilaVacia():
            return False
        else:
            return True, self.elementos[len(self.elementos) - 1]


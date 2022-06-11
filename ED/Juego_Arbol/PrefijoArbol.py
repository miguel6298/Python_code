import os

os.chdir("/Users/miguelruizibanez/Documents/Trabajos_Bioinf/EBD/ED")

from Arbol import Arbol

def Prefijo(arb: Arbol):

    if arb.ArbolVacio():
        print ('.', end='')
    else:
        print (arb.Informacion(), end='')

        Prefijo (arb.HijoIzdo())
        Prefijo (arb.HijoDcho())

def main():
    arb1 = Arbol()
    arb2 = Arbol(1)
    arb3 = Arbol(2, arb1, arb2)

    print (arb3)
    print (arb3.Informacion())

if __name__ == '__main__':
    main()

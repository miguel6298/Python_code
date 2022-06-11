#Autor: Miguel Ruiz Ibáñez

from string import ascii_uppercase

def main():
    A = set()

    for i in ascii_uppercase:
        A.add(i)

    for j in range (0, 9):
        quitar = A.pop()
        print (quitar)

    palabra = input ("Introduzca una palabra para comprobar si sus letras se encuentran en el conjunto A: ")

    for k in palabra:
        if k in A:
            print (k, "está en el conjunto")
        else:
            print (k, "no está en el conjunto")

    for l in range (4):
        letra = input ("Introduzca una letra: ")
        if letra in A:
            A.discard (letra)

    B = set()

    palabraB = input ("Introduzca otra palabra para incluir sus caracteres en el conjunto B: ")
    for i in palabraB:
        B.add(i)

    print (A.union(B))

    if A <= A | B:
        print ("A está en la unión")
    else:
        print ("A no está en la unión")

    if B <= A & B:
        print ("B está en la intersección")
    else:
        print ("B no está en la intersección")

    input ("Pulse <INTRO> para salir.")

if __name__== '__main__':
    main ()
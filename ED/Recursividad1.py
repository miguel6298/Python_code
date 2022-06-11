def Combi(a:int, b:int) -> int:
    
    if b == 0 or a == 0:
        res = 1
    else:
        res = Combi(a - 1, b - 1) + Combi(a - 1, b)

    return res


#SUMAR DÍGITOS:
def SumarDigitos(num: int) -> int: ##Mirar porque cuando pasa de 10 la suma no funciona bien.

    if num < 10:
        res = num
    else:
        res = SumarDigitos(num // 10 + num % 10)
    
    return res



def main():
    """
    m = int (input ("Dame un número entero:"))
    n = int (input ("Dame otro número entero:"))
    num = Combi(m, n)
    print (num)
    """

    num = int (input ("Número : "))
    suma = SumarDigitos(num)
    print (suma)


if __name__ == '__main__':
    main()

print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()
print ("En este programa se va a definir una función que recibirá una cadena de ADN y la convertirá a minúsculas, eliminará espacios y dará la longitud final.")

def filtra ():
    sec_adn = input ("Cadena de ADN: ")
    sec_adn = sec_adn.lower()

    for i in sec_adn:
        if i == " ":
            sec_adn = sec_adn.replace (" ", "")
    
    print (sec_adn)
    print (len (sec_adn))
    return

filtra ()
    

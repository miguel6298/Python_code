
def mutaciones(s1, s2):
    lista = []
    
    if len(s1) <= len(s2):
        rangoSec = len(s1)
    else:
        rangoSec = len(s2)

    for i in range (rangoSec):
        if s1[i] != s2[i]:
            lista.append(i)
    
    return lista

def main():
    sec1 = "ATTTTGCAGTAGTGCTGATCGTAGCTTAGTCGA"
    sec2 = "TTTTATAGGATGATGATGAATAGATAGGCTCTCTCGTCCC"
    mutaciones(sec1, sec2)

    print (mutaciones(sec1, sec2))

if __name__ == '__main__':
    main()

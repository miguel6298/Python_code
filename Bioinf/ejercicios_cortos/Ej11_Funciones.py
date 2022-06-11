print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()

def cuenta_mutaciones(s1,s2): 
    s1 = s1.upper()
    s2 = s2.upper()
    dicc_mut = {"A->T": 0,   
                "A->G": 0,
                "A->C": 0,
                "T->A": 0,
                "T->G": 0,
                "T->C": 0,
                "G->A": 0,
                "G->T": 0,
                "G->C": 0,
                "C->A": 0,
                "C->T": 0,
                "C->G": 0}
    for i,j in zip(s1,s2): 
        if i == "A": 
            if j == "T": 
                dicc_mut ["A->T"] += 1
            if j == "G":
                dicc_mut ["A->G"] += 1
            if j == "C":
                dicc_mut ["A->C"] += 1
        elif i == "T": 
             if j == "A": 
                dicc_mut ["T->A"] += 1
             if j == "G":
                dicc_mut ["T->G"] += 1
             if j == "C":
                dicc_mut ["T->C"] += 1
        elif i == "G": 
             if j == "A": 
                dicc_mut ["G->A"] += 1
             if j == "T":
                dicc_mut ["G->T"] += 1
             if j == "C":
                dicc_mut ["G->C"] += 1
        elif i == "C": 
             if j == "A": 
                dicc_mut ["C->A"] += 1
             if j == "T":
                dicc_mut ["C->T"] += 1
             if j == "G":
                dicc_mut ["C->G"] += 1
    return dicc_mut

sec1 = "AGCTGATCGATGCTAGGGATGCTA"
sec2 = "ATTTATTATAGCGATGCTAGTCGATGCTAG"
print (cuenta_mutaciones(sec1, sec2))

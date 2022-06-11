print (("#" * 55) + "= MIGUEL RUIZ IBÁÑEZ =" + ("#" * 56))
print ()
 

def muestra_codones(mat):
        Nucleotids = ["U", "C", "A", "G"]
        print ("  ", "   ".join(Nucleotids))
        for k in range (len(Nucleotids)):
            for i in range (len(Nucleotids)):
                if i == 1:
                    print (Nucleotids[k], end = " ")
                else:
                    print ("  ", end = "")
                for j in range (len(Nucleotids)):
                    print (mat[k][j][i], end = "  ")
                print ("")
            print ("    ")

matrizentera = [['AAA', 'AAU', 'AAG', 'AAC'], ['AUA', 'AUU', 'AUG', 'AUC'], ['AGA', 'AGU', 'AGG', 'AGC'], ['ACA', 'ACU', 'ACG', 'ACC'], ['UAA', 'UAU', 'UAG', 'UAC'], ['UUA', 'UUU', 'UUG', 'UUC'], ['UGA', 'UGU', 'UGG', 'UGC'], ['UCA', 'UCU', 'UCG', 'UCC'], ['GAA', 'GAU', 'GAG', 'GAC'], ['GUA', 'GUU', 'GUG', 'GUC'], ['GGA', 'GGU', 'GGG', 'GGC'], ['GCA', 'GCU', 'GCG', 'GCC'], ['CAA', 'CAU', 'CAG', 'CAC'], ['CUA', 'CUU', 'CUG', 'CUC'], ['CGA', 'CGU', 'CGG', 'CGC'], ['CCA', 'CCU', 'CCG', 'CCC']]

print (muestra_codones(matrizentera))

 #Mirar de hacer el 4 y el 5 juntos, hay que hacerlo bien.


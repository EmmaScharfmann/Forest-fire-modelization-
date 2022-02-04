import numpy as np 

def copie_foret(F): #copie de la foret pour ne pas travailler en place
    n,m = F.shape
    Fprime = np.empty([n,m])
    for i in range(n):
        for j in range(m):
            Fprime[i,j] = F[i,j]
    return Fprime

def propagation_autour_un_arbre(i,j,F): #propagation autour d'un arbre (etat 1 : arbre vivant) => (etat 2 : arbre en feu)
    if int(F[i+1,j]) == 1:
        F[i+1,j] = 2
    if int(F[i-1,j]) == 1:
        F[i-1,j] = 2
    if int(F[i,j+1]) == 1:
        F[i,j+1] = 2
    if int(F[i,j-1]) == 1:
        F[i,j-1] = 2
    if int(F[i+1,j-1]) == 1:
        F[i+1,j-1] = 2
    if int(F[i-1,j-1]) == 1:
        F[i-1,j-1] = 2
    if int(F[i-1,j+1]) == 1:
        F[i-1,j+1] = 2    
    if int(F[i+1,j+1]) == 1:
        F[i+1,j+1] = 2 
    return F

def comptage(F): #compte le nombre d'arbres vivants, en feu et reduit en cendre pour savoir si le feu va s'arreter ou pas
    ligne, colonne = F.shape
    liste = [0]*3
    for i in range (ligne) :
        for j in range (colonne) :
            if F[i,j] == 1 or F[i,j] == 2:
                liste[int(F[i,j])-1] += 1
    return liste


def propagation(F):
    Fprime = copie_foret(F) #creation de la nouvelle foret
    ligne, colonne = F.shape
    liste_arbre_feu = [] #liste des arbres en feu de la foret F
    for i in range(1,ligne-1):
        for j in range(1,colonne-1):
            if F[i,j] == 2:
                liste_arbre_feu.append([i,j])
            
    for elt in liste_arbre_feu:
        Fprime = propagation_autour_un_arbre(elt[0],elt[1],Fprime)
        Fprime[elt[0],elt[1]] = 3  #l'arbre brule donc au tour suivant c'est une cendre
    return Fprime

#cette fonction retourne la foret precedente, celle que l'on vient de calculer, et la difference d'arbre vivant entre les 2 forets : 
# si ce nombre est nul, le feu s'est arreter : en effet, plus aucun arbre vivant ne prend feu
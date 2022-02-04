import numpy as np
import random as rd

def creation_foret_vide(taille) :
    shape=(taille,taille)
    foret=np.zeros(shape, dtype=int)
    return foret

def creation_foret_aleatoire(taille) :
    foret = creation_foret_vide(taille)
    for i in range(1,taille-1) :
        for j in range(1,taille-1) :
            objet=rd.randint(0,1)
            #0 = gazon
            #1 = arbre
            #2 = en feu
            #3 = cendres
            foret[i][j] = objet
    return foret
    
def mise_a_feu(foret) :
    n, m = foret.shape
    for i in range(1,n-1) :
        foret[1][i] = 2
    return foret
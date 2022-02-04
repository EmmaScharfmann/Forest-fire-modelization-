import numpy as np 
from propagation import *
from dictionnaire import *
import random as rd
import copy

def creation_foret_parametre(taille, liste_arbre_et_pourcentage, densite) :
    foret = [[[] for i in range(taille)] for j in range(taille)]

    for i in range(taille): #ligne
        for j in range(taille): #colonne
            if i == 0 or i == taille-1 or j == 0 or j == taille-1:
                foret[i][j].append(0)
                foret[i][j].append('Prairie')
            else :
                if rd.random() <= densite:
                    foret[i][j].append(1)
                    type_arbre = rd.random()
                    somme = 0
                    indice = 0
                    while type_arbre > somme :
                        somme += liste_arbre_et_pourcentage[indice][1]
                        indice += 1
                    foret[i][j].append(liste_arbre_et_pourcentage[indice - 1][0])
                        
                else:
                    foret[i][j].append(0)
                    foret[i][j].append('Prairie')

    return foret

# Exemple d'utilisation : creation_foret_parametre(10, [['tilleul',0.3],['chene',0.4],['platane',0.3]],1)
#
# Resultat : 

# [[[0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'platane'], [1, 'platane'], [1, 'tilleul'], [1, 'chene'], [1, 'platane'], [1, 'chene'], [1, 'platane'], [1, 'chene'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'tilleul'], [1, 'tilleul'], [1, 'chene'], [1, 'chene'], [1, 'chene'], [1, 'tilleul'], [1, 'platane'], [1, 'chene'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'tilleul'], [1, 'chene'], [1, 'chene'], [1, 'platane'], [1, 'chene'], [1, 'tilleul'], [1, 'chene'], [1, 'chene'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'platane'], [1, 'tilleul'], [1, 'chene'], [1, 'chene'], [1, 'chene'], [1, 'chene'], [1, 'platane'], [1, 'chene'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'platane'], [1, 'chene'], [1, 'chene'], [1, 'platane'], [1, 'platane'], [1, 'tilleul'], [1, 'platane'], [1, 'tilleul'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'platane'], [1, 'chene'], [1, 'platane'], [1, 'tilleul'], [1, 'chene'], [1, 'chene'], [1, 'chene'], [1, 'platane'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'platane'], [1, 'tilleul'], [1, 'tilleul'], [1, 'chene'], [1, 'platane'], [1, 'platane'], [1, 'chene'], [1, 'tilleul'], [0, 'prairie']], 
#  [[0, 'prairie'], [1, 'tilleul'], [1, 'platane'], [1, 'platane'], [1, 'tilleul'], [1, 'tilleul'], [1, 'tilleul'], [1, 'tilleul'], [1, 'tilleul'], [0, 'prairie']], 
#  [[0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie'], [0, 'prairie']]]



def propagation_autour_un_arbre_parametres(indice_ligne,indice_colonne,F,type_vent, force): #propagation prenant de nouveaux parametres
    
    vent = dictionnaire_vent[type_vent] #liste 
    probabilite_vent = []

    for i in range (9) : #il y a 9 elements dans la liste vent
        probabilite_vent.append(1 + vent[i] * force * (1/100))

    if int(F[indice_ligne - 1][indice_colonne - 1][0]) == 1 : #en haut a gauche de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne - 1][indice_colonne - 1][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[0] * probabilite_liee_a_arbre) : 
            F[indice_ligne - 1][indice_colonne - 1][0] = 2
    
    if int(F[indice_ligne - 1][indice_colonne][0]) == 1 : #en haut de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne - 1][indice_colonne][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[1] * probabilite_liee_a_arbre) : 
            F[indice_ligne - 1][indice_colonne][0] = 2
    
    if int(F[indice_ligne - 1][indice_colonne + 1][0]) == 1 : #en haut a droite de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne - 1][indice_colonne + 1][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[2] * probabilite_liee_a_arbre) : 
            F[indice_ligne - 1][indice_colonne + 1][0] = 2

    if int(F[indice_ligne][indice_colonne - 1][0]) == 1 : #a gauche de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne][indice_colonne - 1][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[3] * probabilite_liee_a_arbre) : 
            F[indice_ligne][indice_colonne - 1][0] = 2

    if int(F[indice_ligne][indice_colonne + 1][0]) == 1 : #a droite de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne][indice_colonne + 1][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[5] * probabilite_liee_a_arbre) : 
            F[indice_ligne][indice_colonne + 1][0] = 2

    if int(F[indice_ligne + 1][indice_colonne - 1][0]) == 1 : #en bas a gauche de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne + 1][indice_colonne - 1][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[6] * probabilite_liee_a_arbre) : 
            F[indice_ligne + 1][indice_colonne - 1][0] = 2

    if int(F[indice_ligne + 1][indice_colonne][0]) == 1 : #en dessous de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne + 1][indice_colonne][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[7] * probabilite_liee_a_arbre) : 
            F[indice_ligne + 1][indice_colonne][0] = 2

    if int(F[indice_ligne + 1][indice_colonne + 1][0]) == 1 : #en bas a droite de l'arbre etudie
        probabilite_liee_a_arbre = dictionnaire_arbre[F[indice_ligne + 1][indice_colonne + 1][1]]
        proba_feu = rd.random()
        if proba_feu <= (probabilite_vent[8] * probabilite_liee_a_arbre) : 
            F[indice_ligne + 1][indice_colonne + 1][0] = 2
    return F

def propagation_parametre(F, type_vent, force, capacite_pompier) : 

    Fprime = copy.deepcopy(F) #creation de la nouvelle foret
    ligne, colonne = len(F), len(F)
    liste_arbre_feu = [] #liste des arbres en feu de la foret F
    for i in range(1,ligne-1):
        for j in range(1,colonne-1):
            if F[i][j][0] == 2:
                liste_arbre_feu.append([i,j])
    liste_arbre_feu = intervention_pompiers(liste_arbre_feu, capacite_pompier)[0]
    liste_arbre_sauve = intervention_pompiers(liste_arbre_feu, capacite_pompier)[1]
    for elt in liste_arbre_sauve :
        Fprime[elt[0]][elt[1]][0] = 3
    for elt in liste_arbre_feu:
        Fprime = propagation_autour_un_arbre_parametres(elt[0], elt[1], Fprime, type_vent, force)
        Fprime[elt[0]][elt[1]][0] = 3  #l'arbre brule donc au tour suivant c'est une cendre

    return Fprime

def ajout_graine_a_univers(graine, univers, position_du_feu_x, position_du_feu_y):
    seed=dictionnaire_seed[graine]
    n,m = len(seed), len(seed[0])
    #try :
    for i in range(n-1):
        for j in range(m-1):
            if seed[i][j] == 2 :
                univers[i+position_du_feu_x+1][j+position_du_feu_y+1][0]=seed[i][j]
    return univers
    #except:
        #print("Fais attention a la taille de ton univers")

def intervention_pompiers(liste_arbre_feu, capacite_pompier) :
    taille = len(liste_arbre_feu)
    intervention = int(capacite_pompier * taille)
    liste_arbre_sauve = []
    for i in range(intervention) :
        arbre_sauve = choice(liste_arbre_feu)
        liste_arbre_sauve.append(arbre_sauve)
        liste_arbre_feu.remove(arbre_sauve)
    return liste_arbre_feu, liste_arbre_sauve
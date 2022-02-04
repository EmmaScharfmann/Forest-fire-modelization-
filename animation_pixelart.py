import affichage_unites_pixelart as pix
from propagation_parametres import *
from dictionnaire import *
from argument import *
from tkinter import *

def animation_pixelart(taille, densite, iterations, intervalle, position_du_feu_x, position_du_feu_y,
                        force_du_vent, type_de_vent, chene, platane, pin, bouleau, olivier, vigne,
                        eucalyptus, chataigner, tilleul, erable, frene, robinier, pompier, seed) :

    def update_objet_tkinter(canvas, objet_tkinter, liste_objet, image) : #Prend en parametre l'objet et son canvas, pour changer ses graphismes en fonction de son statut
        #liste_objet est la liste retenant les informations sur l'objet dans chaque case
        #ex : liste_objet [1, 'nom_de_l'arbre']

        int_objet, str_objet = liste_objet[0], liste_objet[1]
        if int_objet == 2 :
            str_objet = "Feu"
        elif int_objet == 3 :
            str_objet = "Cendres"
            
        canvas, objet_tkinter, image = pix.changer_objet(canvas, objet_tkinter, str_objet)

        return canvas, objet_tkinter, image

    def update_canvas_tkinter(foret, canvas, liste_objets_tkinter, liste_images) : #Prend en parametre la foret suivante et le canvas et renvoie le canvas suivant
        n=len(foret)
        for i in range(n) :
            for j in range(n) :
                objet_tkinter = liste_objets_tkinter[i][j]
                image = liste_images[i][j]
                liste_objet = foret[i][j]
                canvas, liste_objets_tkinter[i][j], liste_images[i][j] = update_objet_tkinter(canvas, objet_tkinter, liste_objet, image)
        liste_foret.pop()
        if len(liste_foret) > 0 :
            canvas.after(intervalle, update_canvas_tkinter, liste_foret[len(liste_foret)-1], canvas, liste_objets_tkinter, liste_images)
    
    window = Tk()

    #Initialisation de la foret
    liste_arbre_et_pourcentages=[]
    liste_arbre_et_pourcentages.append(['Chene', chene])
    liste_arbre_et_pourcentages.append(['Platane', platane])
    liste_arbre_et_pourcentages.append(['Pin', pin])
    liste_arbre_et_pourcentages.append(['Bouleau', bouleau])
    liste_arbre_et_pourcentages.append(['Olivier', olivier])
    liste_arbre_et_pourcentages.append(['Vigne', vigne])
    liste_arbre_et_pourcentages.append(['Eucalyptus', eucalyptus])
    liste_arbre_et_pourcentages.append(['Chataignier', chataigner])
    liste_arbre_et_pourcentages.append(['Tilleul', tilleul])
    liste_arbre_et_pourcentages.append(['Erable', erable])
    liste_arbre_et_pourcentages.append(['Frene', frene])
    liste_arbre_et_pourcentages.append(['Robinier', robinier])

    foret = creation_foret_parametre(taille, liste_arbre_et_pourcentages, densite)
    liste_foret = [foret]
    liste_foret.append(ajout_graine_a_univers("petit_ovale_ouest", foret, position_du_feu_x, position_du_feu_y))
    for i in range(iterations) :
        foret = propagation_parametre(foret, type_de_vent, force_du_vent, pompier)
        liste_foret.append(foret)
    liste_foret=liste_foret[::-1]

    #Lancement de l'animation
    canvas, liste_objets_tkinter, liste_images = pix.creation_foret_tkinter(foret, window)
    canvas.after(500, update_canvas_tkinter, liste_foret[len(liste_foret)-1], canvas, liste_objets_tkinter, liste_images)
    canvas.grid()

    window.mainloop()

#animation_pixelart(50, 0.9, 50, 100, 10, 10, 50, "Ouest", 0, 0, 0, 0, 0.3, 0.2, 0.3, 0.1, 0.1, 0, 0, 0, 0, "carre")

animation_pixelart(50, 0.9, 50, 100, 10, 10, 50, "Ouest", 0, 0, 0, 0, 0.3, 0.2, 0.3, 0.1, 0.1, 0, 0, 0, 0, "carre")
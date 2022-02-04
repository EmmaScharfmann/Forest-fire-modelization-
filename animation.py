from propagation import *
from affichage_unites import *
from foret import *
from tkinter import *

def animation(taille, iterations) :

    def update_objet_tkinter(canvas, objet, i, j, int_objet_next) : #Prend en parametre l'objet et son canvas, pour changer ses graphismes en fonction de son statut
        if int_objet_next == 0 :
            canvas, objet = changer_objet_en_prairie(canvas, objet)
        elif int_objet_next == 1 :
            canvas, objet = changer_objet_en_arbre(canvas, objet)
        elif int_objet_next == 2 :
            canvas, objet = changer_objet_en_zone_en_feu(canvas, objet)
        elif int_objet_next == 3 :
            canvas, objet = changer_objet_en_zone_brulee(canvas, objet)

        return canvas, objet

    def update_canvas_tkinter(foret, canvas, liste_objets) : #Prend en parametre la foret suivante et le canvas et renvoie le canvas suivant
        n=len(foret)
        for i in range(n) :
            for j in range(n) :
                objet = liste_objets[i][j]
                int_objet_next = foret[i][j]
                canvas, liste_objets[i][j] = update_objet_tkinter(canvas, objet, i, j, int_objet_next)
        liste_foret.pop()
        if len(liste_foret) > 0 :
            canvas.after(300, update_canvas_tkinter, liste_foret[len(liste_foret)-1], canvas, liste_objets)
    
    window = tk.Tk()

    #Initialisation de la foret
    foret = creation_foret_aleatoire(taille)
    liste_foret = [foret]
    liste_foret.append(mise_a_feu(foret))
    for i in range(iterations) :
        foret = propagation(foret)
        liste_foret.append(foret)
    liste_foret=liste_foret[::-1]

    #Lancement de l'animation
    canvas, liste_objets = creation_foret_tkinter(foret, window)
    canvas.after(300, update_canvas_tkinter, liste_foret[len(liste_foret)-1], canvas, liste_objets)
    canvas.grid()

    window.mainloop()

animation(70, 50)
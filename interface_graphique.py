import tkinter as tk
from tkinter import Frame
from tkinter import Tk, StringVar, Label, Entry, Button
from functools import partial
from argument import *
from animation_pixelart import *


def affichage():
    animation_pixelart(int(size.get()), float(densite.get()), int(nombre_iteration.get()), int(intervalle.get()), int(position_du_feu_x.get()), int(position_du_feu_y.get()), int(force_du_vent.get()), type_de_vent.get(), float(chene.get()), float(platane.get()), float(pin.get()), float(bouleau.get()), float(olivier.get()), float(vigne.get()), float(eucalyptus.get()), float(chataigner.get()), float(tilleul.get()), float(erable.get()), float(frene.get()), float(robinier.get()), float(pompier.get()), seed.get())


root = tk.Tk()
window = tk.Frame(root)
window.pack()

titre = Label(window,text=" SIMULATION D'UN FEU DE FORÊT ")
espace1 = Label(window,text="  " )
descripiton = Label(window,text="Cette animation modélise la propagation d'un feu de forêt en prenant ern compte divers paramètres :")
description1 = Label(window,text="- la taille de la forêt, qui est un entier qui donne la taille de la forêt, par défaut 100")
description2 = Label(window,text="- la densité de la forêt, qui est un entier entre 0 et 1, qui correspond à la densité d'arbre dans la forêt, par défaut 0.5")
description3 = Label(window,text="- le nombre d'itérations, qui est un entier, par défaut 30")
description4 = Label(window,text="- la position du foyer du feu en abscisse, qui est un entier entre 0 et la taille de la forêt, par défaut 0")
description5 = Label(window,text="- la position du foyer du feu en ordonnée, qui est un entier entre 0 et la taille de la forêt, par défaut 0")
description6 = Label(window,text= "- la force du vent, qui donne la force du vent entre 0 et 100, par défaut 0")
description7 = Label(window,text= "- la force du vent, qui donne la force du vent entre 0 et 100, par défaut 0")
description8 = Label(window,text= "- la direction du vent, cela peut être un vent d'Ouest, d'Est, du Nord ou du Sud, neutre, sud-ouest, nord-est, nord-ouest, sud-est ")
description9 = Label(window,text= "- la capacité d'intervention des pompiers, entre 0 et 1")
description10 = Label(window,text="-type de seed : ovale_vent_d_est, ovale_vent_ouest, ovale_bordure, centralesupelec, TJ, ")
description11 = Label(window,text="petit_ovale_ouest, petit_ovale_sud, petit_ovale_est, petit_ovale_nord,  un_seul_arbre, carre")


espace2 = Label(window,text="  " )
espace3 = Label(window,text="  " )



size = tk.StringVar(root)
densite = tk.StringVar(root)
nombre_iteration = tk.StringVar(root)
intervalle = tk.StringVar(root)
position_du_feu_x = tk.StringVar(root)
position_du_feu_y = tk.StringVar(root)
force_du_vent = tk.StringVar(root)
type_de_vent = tk.StringVar(root)
chene = tk.StringVar(root)
platane = tk.StringVar(root)
pin = tk.StringVar(root)
bouleau = tk.StringVar(root)
olivier = tk.StringVar(root)
vigne = tk.StringVar(root)
eucalyptus = tk.StringVar(root)
chataigner = tk.StringVar(root)
tilleul = tk.StringVar(root)
erable = tk.StringVar(root)
frene = tk.StringVar(root)
robinier = tk.StringVar(root)
pompier = tk.StringVar(root)
seed = tk.StringVar(root)

label_size = tk.Label(window, text = 'taille de la forêt : ')
entry_size = tk.Entry(window, textvariable = size)

label_densite = tk.Label(window, text = 'densite de la forêt : ')
entry_densite = tk.Entry(window, textvariable = densite)

label_nombre_iteration = tk.Label(window, text = "nombre d'iterations souhaitees : ")
entry_nombre_iteration = tk.Entry(window, textvariable = nombre_iteration)

label_intervalle = tk.Label(window, text = 'interalle de temps entre 2 iterations : ')
entry_intervalle = tk.Entry(window, textvariable = intervalle)

label_position_du_feu_x = tk.Label(window, text = 'abscisse du foyer du feu : ')
entry_position_du_feu_x = tk.Entry(window, textvariable = position_du_feu_x)

label_position_du_feu_y = tk.Label(window, text = 'ordonnee du foyer du feu : ')
entry_position_du_feu_y = tk.Entry(window, textvariable = position_du_feu_y)

label_force_de_vent = tk.Label(window, text = 'force du vent : ')
entry_force_du_vent = tk.Entry(window, textvariable = force_du_vent)

label_type_de_vent = tk.Label(window, text = 'type de vent : ')
entry_type_de_vent = tk.Entry(window, textvariable = type_de_vent)

label_chene = tk.Label(window, text = 'pourcentage de chêne ')
entry_chene = tk.Entry(window, textvariable = chene)

label_platane = tk.Label(window, text = 'pourcentage de platane ')
entry_platane = tk.Entry(window, textvariable = platane)

label_bouleau = tk.Label(window, text = 'pourcentage de bouleau ')
entry_bouleau = tk.Entry(window, textvariable = bouleau)

label_pin = tk.Label(window, text = 'pourcentage de pin ')
entry_pin = tk.Entry(window, textvariable = pin)

label_robinier = tk.Label(window, text = 'pourcentage de robinier ')
entry_robinier = tk.Entry(window, textvariable = robinier)

label_olivier = tk.Label(window, text = 'pourcentage de olivier ')
entry_olivier = tk.Entry(window, textvariable = olivier)

label_frene = tk.Label(window, text = 'pourcentage de frêne ')
entry_frene = tk.Entry(window, textvariable = frene)

label_erable = tk.Label(window, text = 'pourcentage de érable ')
entry_erable = tk.Entry(window, textvariable = erable)

label_tilleul = tk.Label(window, text = 'pourcentage de tilleul ')
entry_tilleul = tk.Entry(window, textvariable = tilleul)

label_chataigner = tk.Label(window, text = 'pourcentage de chataigner ')
entry_chataigner = tk.Entry(window, textvariable = chataigner)


label_eucalyptus = tk.Label(window, text = 'pourcentage de eucalyptus ')
entry_eucalyptus = tk.Entry(window, textvariable = eucalyptus)

label_vigne = tk.Label(window, text = 'pourcentage de vigne ')
entry_vigne = tk.Entry(window, textvariable = vigne)

label_pompier = tk.Label(window, text = "capacité d'intervention des pompiers ")
entry_pompier = tk.Entry(window, textvariable = pompier)

label_seed = tk.Label(window, text = "type de commencement d'incendie" )
entry_seed = tk.Entry(window, textvariable = seed)






button = tk.Button(window, text='lancer l animation' , command= affichage)


label_size.grid(column=0, row=15)
entry_size.grid(column=0, row=16)

label_densite.grid(column=1, row=15)
entry_densite.grid(column=1, row=16)

label_nombre_iteration.grid(column=2, row=15)
entry_nombre_iteration.grid(column=2, row=16)

label_intervalle.grid(column=0, row=18)
entry_intervalle.grid(column=0, row=19)

label_position_du_feu_x.grid(column=1, row=18)
entry_position_du_feu_x.grid(column=1, row=19)

label_position_du_feu_y.grid(column=2, row=18)
entry_position_du_feu_y.grid(column=2, row=19)

label_force_de_vent.grid(column=0, row=22)
entry_force_du_vent.grid(column=0, row=23)

label_type_de_vent.grid(column=1, row=22)
entry_type_de_vent.grid(column=1, row=23)

label_chene.grid(column=2, row=22)
entry_chene.grid(column=2, row=23)

label_bouleau.grid(column=0, row=27)
entry_bouleau.grid(column=0, row=28)

label_pin.grid(column=1, row=27)
entry_pin.grid(column=1, row=28)

label_platane.grid(column=2, row=27)
entry_platane.grid(column=2, row=28)

label_robinier.grid(column=0, row=32)
entry_robinier.grid(column=0, row=33)

label_olivier.grid(column=1, row=32)
entry_olivier.grid(column=1, row=33)

label_frene.grid(column=2, row=32)
entry_frene.grid(column=2, row=33)

label_erable.grid(column=0, row=37)
entry_erable.grid(column=0, row=38)

label_tilleul.grid(column=1, row=37)
entry_tilleul.grid(column=1, row=38)


label_chataigner.grid(column=2, row=37)
entry_chataigner.grid(column=2, row=38)

label_eucalyptus.grid(column=0, row=42)
entry_eucalyptus.grid(column=0, row=43)

label_vigne.grid(column=1, row=42)
entry_vigne.grid(column=1, row=43)

label_seed.grid(column=2, row=42)
entry_seed.grid(column=2, row=43)

label_pompier.grid(column=0, row=44)
entry_pompier.grid(column=0, row=45)



button.grid(column=1, row=45)

titre.grid(column=1, row=0)
espace1.grid(column=0, row=1)

descripiton.grid(column=1, row=2)
description1.grid(column=1, row=3)
description2.grid(column=1, row=4)
description3.grid(column=1, row=5)
description4.grid(column=1, row=6)
description5.grid(column=1, row=7)
description6.grid(column=1, row=8)
description7.grid(column=1, row=9)
description8.grid(column=1, row=10)
description9.grid(column=1, row=11)
description10.grid(column=1, row=12)
description11.grid(column=1, row=13)


espace2.grid(column=1, row=14)
espace3.grid(column=1, row=44)

window.mainloop()



##la fenêtre graphique est finie, il faut mettre la bonne fonction dans le bouton pour lancer l'animation ! 

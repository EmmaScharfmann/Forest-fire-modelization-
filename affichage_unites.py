import tkinter as tk 

#Dessins des objets

def dessiner_arbre(abscisse, ordonnee, canvas):
    arbre = canvas.create_rectangle((abscisse*10,ordonnee*10), (abscisse*10+10, ordonnee*10+10), width=0, fill="green")
    return arbre

def dessiner_prairie(abscisse, ordonnee, canvas):
    prairie = canvas.create_rectangle((abscisse*10, ordonnee*10), (abscisse*10+10, ordonnee*10+10), width=0, fill="#7CFC00" )
    return prairie

def dessiner_zone_en_feu(abscisse, ordonnee, canvas):
    zone_en_feu = canvas.create_rectangle((abscisse*10, ordonnee*10), (abscisse*10+10, ordonnee*10+10), width = 0, fill="orange")
    return zone_en_feu

def dessiner_zone_brulee(abscisse, ordonnee, canvas):
    zone_brulee = canvas.create_rectangle((abscisse*10, ordonnee*10), (abscisse*10+10, ordonnee*10+10), width = 0, fill = "black")
    return zone_brulee

#Changement des objets

def changer_objet_en_arbre(canvas, objet) :
    canvas.itemconfig(objet, fill = "green")
    return canvas, objet 

def changer_objet_en_prairie(canvas, objet) :
    canvas.itemconfig(objet, fill = "#7CFC00")
    return canvas, objet

def changer_objet_en_zone_en_feu(canvas ,objet) :
    canvas.itemconfig(objet, fill = "orange")
    return canvas, objet

def changer_objet_en_zone_brulee(canvas, objet) :
    canvas.itemconfig(objet, fill= "black")
    return canvas, objet

#Fonction de creation de la foret initiale
def creation_foret_tkinter(universe, window):
    n=len(universe)
    canvas = tk.Canvas(window, bg="white", height=n*10, width=n*10)
    n=len(universe)
    l=[]
    for i in range(n):
        p=[]
        for j in range(n):
            if universe[i][j]==0:
                dessiner_prairie(i,j,canvas)
                p.append(dessiner_prairie(i,j,canvas))
            elif universe[i][j]==1:     
                dessiner_arbre(i,j, canvas)  
                p.append(dessiner_arbre(i,j, canvas))
            elif universe[i][j]==2 :
                dessiner_zone_en_feu(i,j,canvas)
                p.append(dessiner_zone_en_feu(i,j,canvas))
            else : 
                dessiner_zone_brulee(i,j,canvas)
                p.append(dessiner_zone_brulee(i,j,canvas))
        l.append(p)
    return canvas, l
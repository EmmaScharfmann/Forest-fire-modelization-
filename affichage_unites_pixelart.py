import tkinter as tk

def dessiner_objet(abscisse, ordonnee, canvas, str_objet) :
    path = "../graphismes/"+str_objet+".png"
    image = tk.PhotoImage(file = path)
    objet_tkinter = canvas.create_image(abscisse*20, ordonnee*20, image=image)
    return canvas, objet_tkinter, image

def changer_objet(canvas, objet_tkinter, objet) :
    path = "../graphismes/"+objet+".png"
    image = tk.PhotoImage(file = path)
    canvas.itemconfig(objet_tkinter, image = image)
    return canvas, objet_tkinter, image

#Fonction de creation de la foret initiale
def creation_foret_tkinter(universe, window):
    n=len(universe)
    canvas = tk.Canvas(window, bg="white", height=n*20, width=n*20)
    n=len(universe)
    liste_objets_tkinter=[]
    liste_images=[]
    for i in range(n):
        objets_tmp=[]
        images_tmp=[]
        for j in range(n):
            str_objet = universe[i][j][1]
            canvas, objet_tkinter, image = dessiner_objet(i,j,canvas,str_objet)
            objets_tmp.append(objet_tkinter)
            images_tmp.append(image)
        liste_objets_tkinter.append(objets_tmp)
        liste_images.append(images_tmp)
    return canvas, liste_objets_tkinter, liste_images


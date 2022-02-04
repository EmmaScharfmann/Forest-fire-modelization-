import argparse

def argument() :

    #Configuration des options

    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--size", help="un entier qui donne la taille de la foret, par defaut a 100", type=int)
    parser.add_argument("-d","--densite", help="densite de la foret, par defaut 0.5")
    parser.add_argument("-n","--nombre_iteration", help="nombre d'iterations, par defaut 30", type=int)
    parser.add_argument("-i","--intervalle", help="intervalle de temps entre deux images en ms, 300 par defaut", type=int)
    parser.add_argument("-px","--position_du_feu_x", help =" position initiale du feu en abscisse", type=int)
    parser.add_argument("-py","--position_du_feu_y", help =" position initiale du feu en ordonnee", type=int)
    parser.add_argument("-f", "--force_du_vent", help= "donne la force du vent entre 0 et 100", type = int)
    parser.add_argument("-t", "--type_de_vent", help = "s'agit-il d'un vent d'ouest, d'est, du Nord ou du Sud?", type = str)
    
    args = parser.parse_args()

    #Valeurs par defaut

    if not args.size :
        args.size = 100

    if not args.densite :
        args.densite = 0.5

    if not args.nombre_iteration :
        args.nombre_iteration=30

    if not args.intervalle :
        args.intervalle = 300

    if not args.position_du_feu_x:
        args.position_du_feu = 0

    if not args.position_du_feu_y:
        args.position_du_feu = 0

    if not args.force_du_vent :
        args.force_du_vent = 0

    if not args.type_de_vent :
        args.type_de_vent = "Ouest"

    return args.size, args.densite, args.nombre_iteration, args.intervalle, args.position_du_feu_x, args.position_du_feu_y, args.force_du_vent, args.type_de_vent


if __name__== "__argument__" :
    argument()
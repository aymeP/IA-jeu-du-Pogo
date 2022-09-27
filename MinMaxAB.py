#Importer fichier
from ValeurCoup import *
from Constantes import *
from Changer import changementCouleur
from ClassePlateau import *


#Algo MinMax ac elagage alpha beta
def minMaxAB(plateau, couleurJoueur, profondeur):
    """Fonction de recherche MinMax avec elagage Alpha-Beta"""
    coupsSuivants=plateau.prochains(couleurJoueur)#genere tous les coups suivants possibles
    valeurCoup=[]
    for coup in coupsSuivants:
        #pour chaque coup suivant possible, la fonction recherche sa valeur et la sauvegarde dans le tableau valeurCoup
        valeurCoup.append(valeurMaxAB(coup, changementCouleur(couleurJoueur), profondeur-1, borneMin, borneMax, plateau))
    meilleurCoup=valeurCoup.index(max(valeurCoup))#Recherche l'emplacement de la valeur la plus elevee des coups suivants
    return coupsSuivants[meilleurCoup]#Retourne le meilleur coup a jouer, celui avec la valeur de valeurCoup la plus elevee


def valeurMaxAB(coup, couleurJoueur, profondeur, alpha, beta, plateau):
    """Recherche la valeur max avec elagage Alpha-Beta"""
    if(coup.gagnant(couleurJoueur) or profondeur==0):
        return valeur(coup, couleurJoueur,profondeur, plateau)
    v=borneMin
    couleurJoueur=changementCouleur(couleurJoueur)
    for successeur in coup.prochains(couleurJoueur):
        v=max(v, valeurMinAB(successeur, couleurJoueur, profondeur-1, alpha, beta, plateau))
        if(v>=beta):
            return v
        alpha=max(alpha, v)
    return v


def valeurMinAB(coup, couleurJoueur, profondeur, alpha, beta, plateau):
    """Recherche la valeur min avec elagage Alpha-Beta"""
    if(coup.gagnant(couleurJoueur) or profondeur==0):
        return valeur(coup,couleurJoueur,profondeur,plateau)
    v=borneMax
    couleurJoueur=changementCouleur(couleurJoueur)
    for successeur in coup.prochains(couleurJoueur):
        v=min(v, valeurMaxAB(successeur, couleurJoueur, profondeur-1, alpha, beta, plateau))
        if(v<=alpha):
            return v
        beta=min(beta, v)
    return v





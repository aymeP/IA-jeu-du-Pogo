#Importer fichiers
from ValeurCoup import *
from Constantes import *
from Changer import changementCouleur
from ClassePlateau import *


#Algo MinMax ac profondeur limitée
def minMaxPL(plateau, couleurJoueur, profondeur):
    """Fonction de recherche MinMax sans elagage Alpha-Beta"""
    coupsSuivants=plateau.prochains(couleurJoueur)#genere tous les coups suivants possibles
    valeurCoup=[]
    for coup in coupsSuivants:
        #pour chaque coup suivant possible, la fonction recherche sa valeur et la sauvegarde dans le tableau valeurCoup
        valeurCoup.append(valeurMaxPL(coup, changementCouleur(couleurJoueur), profondeur-1, plateau))
    meilleurCoup=valeurCoup.index(max(valeurCoup))#Recherche l'emplacement de la valeur la plus elevee des coups suivants
    return coupsSuivants[meilleurCoup]#Retourne le meilleur coup a jouer, celui avec la valeur de valeurCoup la plus elevee


def valeurMaxPL(coup, couleurJoueur, profondeur, plateau):
    """Recherche la valeur max sans elagage Alpha-Beta"""
    if(coup.gagnant(couleurJoueur) or profondeur==0):
        return valeur(coup, couleurJoueur,profondeur, plateau)
    v=borneMin
    couleurJoueur=changementCouleur(couleurJoueur)
    for successeur in coup.prochains(couleurJoueur):
        v=max(v, valeurMinPL(successeur, couleurJoueur, profondeur-1, plateau))
    return v


def valeurMinPL(coup, couleurJoueur, profondeur, plateau):
    """Recherche la valeur min sans elagage Alpha-Beta"""
    if(coup.gagnant(couleurJoueur) or profondeur==0):
        return valeur(coup,couleurJoueur,profondeur, plateau)
    v=borneMax
    couleurJoueur=changementCouleur(couleurJoueur)
    for successeur in coup.prochains(couleurJoueur):
        v=min(v, valeurMaxPL(successeur, couleurJoueur, profondeur-1, plateau))
    return v

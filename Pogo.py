#Librairies
from ClassePlateau import *
from Saisie import *
from ModesDeJeu import *
from Constantes import couleur


"""Main"""
jouer=1

#Saisie des paramètres pour les fonctions MinMax
elagage,profondeur=parametres()

while(jouer==1):
    
    #Menu principal
    print("Choisir un mode de jeu : \n 1.Joueur vs IA\n 2.IA vs IA\n 3.Parametres\n 4.Quitter")
    modeDeJeu=saisirEntier(1,4)

    #Déroulement partie
    if(modeDeJeu in [1,2]):
        if(modeDeJeu==1):
            JoueurvsIA(plateauJeu, couleur, elagage, profondeur)
        else:
            IAvsIA(plateauJeu, couleur, elagage, profondeur)
        #Revenir au menu ou Quitter
        print("\n\nSuite : \n 1.Revenir au menu\n 2.Quitter")
        jouer=saisirEntier(1,2)        
    else:
        if(modeDeJeu==3):
            elagage,profondeur=parametres()
        else:
            jouer=0

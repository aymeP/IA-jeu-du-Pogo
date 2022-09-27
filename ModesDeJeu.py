import copy
from ClassePlateau import *
from MinMaxAB import *
from MinMaxPL import *
from Changer import *
from ControleDeplacement import *
from Saisie import *

def jouerCoupIA(plateauJeu, couleurJoueur, elagage, profondeur):
    """Fonction calculant le meilleur coup à jouer de l'ordinateur"""
    if(elagage):
        return copy.deepcopy(minMaxAB(plateauJeu, couleurJoueur, profondeur))
    else:
        return copy.deepcopy(minMaxPL(plateauJeu, couleurJoueur, profondeur))



def IAvsIA(plateauJeu, couleur, elagage, profondeur):
    """Mode de jeu ordinateur contre lui-meme"""
    tourJoueur=1
    nbCoups=0
    gagne=False
    while(not gagne):
        couleurJoueur=couleur[tourJoueur-1]
        if(tourJoueur==1):
            nbCoups+=1
        plateauJeu=jouerCoupIA(plateauJeu, couleurJoueur, elagage, profondeur)
        print("Tour " + str(nbCoups),": IA"+str(tourJoueur))
        print(plateauJeu)
        if(plateauJeu.gagnant(couleurJoueur)):
            gagne=True
            print("IA" + str(tourJoueur)," gagne !! (" + str(nbCoups)," coups)")
        else:
            tourJoueur=changementJoueur(tourJoueur)



def JoueurvsIA(plateauJeu, couleur, elagage, profondeur):
    """Mode de jeu joueur contre ordinateur"""
    #choix de la couleur du joueur
    print("Quelle couleur voulez-vous jouer : \n 1.Blanc \n 2.Noir")
    couleurJouee=saisirEntier(1,2)

    #afficher plateau
    print("\n\n")
    print(plateauJeu)
    
    #Intialisation variables
    gagne=False
    nbCoups=0.5
    tourJoueur=1 #1 ou 2. Permet de savoir si c'est au joueur ou a l'IA de jouer

    #Jouer une partie
    while(not gagne):
        nbCoups+=0.5
        couleurJoueur=couleur[tourJoueur-1]
        
        
        if(tourJoueur==couleurJouee):
            #tourJoueur est egal à la couleur choisie et jouee par le joueur, donc il joue
            print("Tour " + str(int(nbCoups)),": Vous")
            #Choix et controle du coup joue
            deplacementOK=False
            while(not deplacementOK):
                #Choix de la case de depart
                caseDepart=caseDepPossibles(plateauJeu, couleurJoueur)

                #Choix du nombre de pieces a deplacer
                nbPiecesDeplacees=nbPiecesDepPossibles(plateauJeu, caseDepart)
                
                #Choix de la case d'arrivee
                caseArrivee=caseArriveePossibles(caseDepart, nbPiecesDeplacees)
                
                #Controler le coup joué
                deplacementOK=controleDeplacement(caseDepart,caseArrivee,nbPiecesDeplacees)

                #Si le coup est impossible, on l'annonce et le joueur doit le saisir a nouveau
                if(not deplacementOK):
                    print("Deplacement impossible")

            #Enregistrer le coup joue
            enregistrerCoup(plateauJeu, caseDepart, caseArrivee, nbPiecesDeplacees)


        else:
            #tourJoueur n'est pas egal à la couleur choisie par le joueur donc l'IA joue
            print("Tour " + str(int(nbCoups)),": IA")
            plateauJeu=jouerCoupIA(plateauJeu, couleurJoueur, elagage, profondeur)

             
        #On affiche le coup résultant
        print(plateauJeu)
        
        #on controle si le coup est gagnant
        if(plateauJeu.gagnant(couleurJoueur)):
            #Le coup est gagnant, le vainquer est affiche
            gagne=True
            if(tourJoueur==couleurJouee):
                print("Vous avez gagne !! (" + str(int(nbCoups))," coups)")
            else:
                print("Perdu !! (" + str(int(nbCoups))," coups)")
        else:
            #Le coup n'est pas gagnant, l'autre joueur va jouer
            tourJoueur=changementJoueur(tourJoueur)
            print("********************************************************************************")



def parametres():
    #Avec ou sans elagage alpha beta
    print("Avec elagage alpha beta ?\n 0.Non\n 1.Oui")
    elagage=saisirEntier(0,1)

    #Choix de la profondeur
    print("Saisir la profondeur souhaitee pour l'algorithme minmax : ")
    profondeur=saisirEntier(1,10)

    return elagage, profondeur

    

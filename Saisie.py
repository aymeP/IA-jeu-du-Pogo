#Saisir entier
def saisirEntier(nbMin,nbMax):
    """Controle que la saisie d'un entier soit entre nbMin et nbMax"""
    nbSaisi=-1
    while(nbSaisi<nbMin or nbSaisi>nbMax):
        nbSaisi=input("Saisir entier (entre " + str(nbMin) + " et " + str(nbMax) + ") : ")
        #Convertie la saisie en un entier
        try:
            nbSaisi=int(nbSaisi)
        except ValueError:
            print("Vous n'avez pas saisi un nombre!")
            nbSaisi=-1
    return nbSaisi



#Saisir la caseDepart
def caseDepPossibles(plateauJeu, couleurJoueur):
    """Fonction permettant de saisir la case de depart en vérifiant qu'elle existe (entre 1 et 9)"""
    print("Veuillez choisir la case de Depart de votre déplacement :")
    caseDepart = saisirEntier(1,9)-1 #Nous retirons 1 à la case saisie pour pouvoir directement utiliser la valeur dans notre tableau

    """Controle qu'il y ait une pile de pions sur la case saisie et que le joueur ait bien une piece de sa couleur en haut de la pile"""
    while(len(plateauJeu.plateau[caseDepart]) == 0 or plateauJeu.plateau[caseDepart][0] != couleurJoueur):
        print("Vous n'avez pas de pions sur cette case !")
        caseDepart = saisirEntier(1,9)-1
    return caseDepart



#Saisir le nbPiecesDeplacees
def nbPiecesDepPossibles(plateauJeu, caseDepart):
    """Fonction permettant de saisir le nombre de pions à deplacer en fonction de la taille de la pile de depart (ou 3 au maximum)"""
    print("Veuillez choisir le nombre de pièces à déplacer :")
    nbPiecesDeplacees = saisirEntier(1,min(3,len(plateauJeu.plateau[caseDepart])))
    return nbPiecesDeplacees



#Saisir la caseArrivee
def caseArriveePossibles(caseDepart, nbPiecesDeplacees):
    """Fonction permettant de saisir la case d'arrivee en vérifiant qu'elle existe (entre 1 et 9)"""
    print("Veuillez choisir la case d'arrivée de votre déplacement :")
    caseArrivee = saisirEntier(1, 9)-1 #Nous retirons 1 à la case saisie pour pouvoir directement utiliser la valeur dans notre tableau
    return caseArrivee



#Enregistrer le coup
def enregistrerCoup(plateauJeu, caseDepart, caseArrivee, nbPiecesDeplacees):
    """Fonction permettant d'enregistrer le coup joué"""
    for i in range(nbPiecesDeplacees):
        plateauJeu.plateau[caseArrivee].insert(i,plateauJeu.plateau[caseDepart].pop(0))
    plateauJeu.nbPiecesDep=nbPiecesDeplacees
    plateauJeu.caseDep=caseDepart+1
    plateauJeu.caseArr=caseArrivee+1





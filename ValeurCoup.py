def valeur(coup, couleurJoueur, profondeur, preCoup):
    """attribue une valeur au coup"""
    if(coup.gagnant(couleurJoueur)):#le coup est gagnant
        return 100 + profondeur #l'ajout de la profondeur permet de prioritiser les coups gagnants tout de suite par rapport à ceux
                                #permettant de gagner au prochain coup 
    #le coup n'est pas gagnant, on compte le nombre de pile qui appartiennent au joueur

    ValeurPreCoup=1
    ValeurCoup=0
    Bonus=0

    #On vérifie la difference de valeur du coup pour la case de DEPART
    for index in range(len(preCoup.plateau[preCoup.caseDep-1])):
        if preCoup.plateau[preCoup.caseDep-1][index]!=couleurJoueur:
            ValeurPreCoup+=1
    #---
    if len(coup.plateau[coup.caseDep-1]) and coup.plateau[coup.caseDep-1][0] == couleurJoueur:
        Bonus = 1
        ValeurCoup+=1
    else:
        Bonus = -1
    for index in range(len(coup.plateau[coup.caseDep-1])):
        if coup.plateau[coup.caseDep-1][index]!=couleurJoueur:
            ValeurCoup+=Bonus
    #------------------------------------------------------------

    # On vérifie la difference de valeur du coup pour la case d'ARRIVEE'
    if  len(preCoup.plateau[preCoup.caseArr-1]) and preCoup.plateau[preCoup.caseArr-1][0] == couleurJoueur:
        Bonus = 1
        ValeurPreCoup+=1
    else:
        Bonus = -1
    for index in range(len(preCoup.plateau[preCoup.caseArr-1])):
        if preCoup.plateau[preCoup.caseArr-1][index]!=couleurJoueur:
            ValeurPreCoup+=Bonus
    #---
    for index in range(len(coup.plateau[coup.caseArr-1])):
        if coup.plateau[coup.caseArr-1][index]!=couleurJoueur:
            ValeurCoup+=1
    #-------------------------------------------------------------

    ValeurCoup = ValeurCoup - ValeurPreCoup
    return ValeurCoup


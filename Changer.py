#Changer joueur
def changementJoueur(joueur):
    """Permet d'alterner entre deux joueurs"""
    if joueur==1:
        return 2
    return 1



#Changer couleur
def changementCouleur(couleur):
    """Permet d'alterner entre deux couleurs"""
    if couleur=='b':
        return 'n'
    return 'b'

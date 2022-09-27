def controleDeplacement(dep, arr, nbDep):
    """Controle si un deplacement envisage est autorise ou non"""
    if(dep==arr):
        #Vérifie que la case de départ soit différente de la case d'arrivee
        return False
    if(nbDep==1):
        #Cas ou le joueur deplace un pion
        if (arr-dep in [-1,1,-3,3]):
            if((dep in [3,6] and arr in [2,5]) or (dep in [2,5] and arr in [3,6])):
                return False
            return True
    if(nbDep==2):
        #Cas ou le joueur deplace deux pions
        if (arr-dep in [-6,-4,-2,2,4,6]):
            if((dep==6 and arr==2) or (dep==2 and arr==6)):
                return False
            return True
    if(nbDep==3):
        #Cas ou le joueur deplace trois pions
        if (arr-dep in [-7,-5,-3,-1,1,3,5,7]):
            return True

    return False

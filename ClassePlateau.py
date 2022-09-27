import copy
from ControleDeplacement import *


#classe du plateau de jeu
class plateau:
    def __init__(self):
        """initialise un plateau de jeu"""
        self.plateau=[['b','b'],['b','b'],['b','b'],[],[],[],['n','n'],['n','n'],['n','n']]
        self.nbPiecesDep=0
        self.caseDep=-1
        self.caseArr=-1

    def __repr__(self):
        """Affiche un plateau ou les plateaux suivants possibles"""
        if(self.nbPiecesDep):
            #Si au moins une piece est deplacée, on affiche le coup effectué
            return ("Deplacer {} piece(s) de la case {} à la case {}\n{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n\n".format(self.nbPiecesDep,self.caseDep,self.caseArr,self.plateau[0],self.plateau[1],self.plateau[2],self.plateau[3],self.plateau[4],self.plateau[5],self.plateau[6],self.plateau[7],self.plateau[8]))
        #Sinon, on affiche le plateau actuel
        return ("{}  {}  {}\n{}  {}  {}\n{}  {}  {}\n\n".format(self.plateau[0],self.plateau[1],self.plateau[2],self.plateau[3],self.plateau[4],self.plateau[5],self.plateau[6],self.plateau[7],self.plateau[8]))
        
    def nbPieces(self, case, couleurPiece):
        """Retourne le nombre de pièces d'une pile qu'un joueur peut déplacer (3 au max)"""
        return min(3, len(self.plateau[case]))
    
    def prochains(self,couleurPiece):
        """Retourne les prochains etats possibles à partir de l'etat actuel"""        
        listeProchainsPlateaux=[]

        for caseDepart in range(0,9):
            if len(self.plateau[caseDepart]) and self.plateau[caseDepart][0]==couleurPiece:
                #appelle une fonction qui compte le nbre de pièce que le joueur peut deplacer
                for nbPiecesDeplacees in range(1,self.nbPieces(caseDepart,couleurPiece)+1):
                    for caseArrivee in range (0,9):
                        ##appelle la fonction qui controle si le déplacement est ok ou non
                        if(controleDeplacement(caseDepart, caseArrivee,nbPiecesDeplacees)):
                            #Mettre en forme le prochain etat
                            prochainPlateau = copy.deepcopy(self)
                            for i in range(nbPiecesDeplacees):
                                prochainPlateau.plateau[caseArrivee].insert(i,prochainPlateau.plateau[caseDepart].pop(0))
                            prochainPlateau.nbPiecesDep=nbPiecesDeplacees
                            prochainPlateau.caseDep=caseDepart+1
                            prochainPlateau.caseArr=caseArrivee+1
                            listeProchainsPlateaux.append(prochainPlateau)
        return listeProchainsPlateaux

    def gagnant(self,couleurPiece):
        """Controle si un joueur a une pièce de sa couleur au sommet de chaque pile"""
        for case in range(9):
            if (len(self.plateau[case])):
                if (self.plateau[case][0]!=couleurPiece):
                    return False
        return True



#Variable
plateauJeu=plateau()


from quixo import Quixo
from quixo_error import*


class QuixoIA(Quixo):
    def __init__(self):
        super().__init__()
    
    def valider_diagonale(self, plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        coord_x = []
        coord_o = []
        compteur_X_1 = 0
        compteur_X_2 = 0
        compteur_O_1 = 0
        compteur_O_2 = 0
        for i in range(len(plateau)):
            if (plateau[i][i]).upper() == 'X':
                compteur_X_1 += 1
            if(plateau[i][i]).upper() == 'O':
                compteur_O_1 += 1
            if(plateau[i][4-i]).upper() == 'X':
                compteur_X_2 += 1
            if(plateau[i][4-i]).upper() == 'O':
                compteur_O_2 += 1
        if compteur_X_1 >= nb_pions:
            coord_x.append([[1, 1], [5, 5]])
        if compteur_O_1 >= nb_pions:
            coord_o.append([[1, 1], [5, 5]])
        if compteur_X_2 >= nb_pions:
            coord_x.append([[1, 5], [5, 1]])
        if compteur_O_2 >= nb_pions:
            coord_o.append([[1, 5], [5, 1]])
        resultat = {"X": coord_x , "O": coord_o}
        return resultat
            
    
    def valider_horizontale(self, plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        coord_x = []
        coord_o = []
        for i in range(len(plateau)):
            compteur_X = 0
            compteur_O = 0
            for j in range(len(plateau)):
                if (plateau[i][j]).upper() == 'X':
                    compteur_X += 1
                if(plateau[i][j]).upper() == 'O':
                    compteur_O += 1
            if compteur_X >= nb_pions:
                coord_x.append([[1, i+1], [5, i+1]])
            if compteur_O >= nb_pions:
                coord_o.append([[1, i+1], [5, i+1]])
        resultat = {"X": coord_x , "O":coord_o}
        return resultat
    
    def valider_verticale(self, plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        coord_x = []
        coord_o = []
        for j in range(len(plateau)):
            compteur_X = 0
            compteur_O = 0
            for i in range(len(plateau)):
                if (plateau[i][j]).upper() == 'X':
                    compteur_X += 1
                if(plateau[i][j]).upper() == 'O':
                    compteur_O += 1
            if compteur_X >= nb_pions:
                coord_x.append([[j+1, 1], [j+1, 5]])
            if compteur_O >= nb_pions:
                coord_o.append([[j+1, 1], [j+1, 5]])
        resultat = {"X": coord_x , "O": coord_o}
        return resultat
    
    def partie_terminée(self):
        for f in (self.valider_horizontale, self.valider_verticale, self.valider_diagonale):
            resultat = f(self.plateau)
            for joueur in ['X', 'O']:
                if len(resultat[joueur]) > 0:
                    return joueur
        return None
    
    def pions_jouables(self,plateau, pion):
        jouables  = []
        for i in range(len(plateau)):
            for j in range(len(plateau)):
                if (plateau[i][j]).upper() in [pion.upper(), ' '] and (i in [0, 4] or j in [0, 4]):
                    jouables.append((i,j))
        return jouables

    def trouver_coup_gagnant(self, pion):
        try:
            for f in [self.valider_horizontale, self.valider_verticale, self.valider_diagonale]:
                resultat = f(self.plateau)
                if pion in resultat and resultat[pion]:
                    return resultat[pion]
            raise QuixoError("Aucun coup gagnant possible.")
        except QuixoError as e:
            print(e)
        return None

    def trouver_coup_bloquant(self, pion):
        adversaire = 'O' if pion == 'X' else 'X'
        for i in range(5):
            for j in range(5):
                if self.plateau[i][j] == ' ':
                    self.plateau[i][j] = adversaire
                    if self.partie_terminee() == adversaire:
                        self.plateau[i][j] = ' '
                        return (i, j)
                    self.plateau[i][j] = ' '
        raise QuixoError("Aucun coup bloquant possible.")
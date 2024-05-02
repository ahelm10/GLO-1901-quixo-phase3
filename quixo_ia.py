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
        for j in range(len(plateau[0])):
            compteur_X = 0
            compteur_O = 0
            for i in range(len(plateau)):
                if (plateau[i][j]).upper() == 'X':
                    compteur_X == 0:
                if(plateau[i][j]).upper() == 'O':
                    compteur_O += 1
            if compteur_X >= nb_pions:
                coord_x.append([[1, i+1], [5, i+1]])
            if compteur_O >= nb_pions:
                coord_o.append([[1, i+1], [5, i+1]])
        resultat = {"X": coord_x , "O":coord_o}
        return resultat
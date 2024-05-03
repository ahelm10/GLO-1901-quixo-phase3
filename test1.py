from plateau import *
from quixo_error import*

def test_creation():
    plateau_input = [
        ["X", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", "O", " "],
    ]
    plateau = Plateau(plateau_input)
    print("Plateau initial:")
    print(plateau)
    print (plateau[(5, 4)] == 'O')
    # test de gettim
    plateau[(5, 5)] = 'X'
    print (plateau[(5, 5)] == 'X')
# test de setitem
#test_creation()

def test_insertion():
    plateau_input = [
        ["O", "X", "O", "X", "O"],
        [" ", "O", " ", " ", " "],
        [" ", "X", " ", " ", " "],
        [" ", "O", " ", " ", " "],
        [" ", "X", " ", "O", " "],
    ]
    plateau = plateau(plateau_input)
    plateau.insertion('O', [5, 5], 'bas')
    print(plateau)

#test_insertion()
#test_creation()

def valider_diagonale(plateau, nb_pions=5):
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
            
    
def valider_horizontale(plateau, nb_pions=5):
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

def valider_verticale(plateau, nb_pions=5):
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

def partie_terminée(plateau):
    for f in (valider_horizontale, valider_verticale, valider_diagonale):
        resultat = f(plateau)
        for joueur in ['X', 'O']:
            if len(resultat[joueur]) > 0:
                return joueur
    return None



def partie_terminee2(plateau):
    gagnant = None
    dict_diag = valider_diagonale(plateau, 5)
    dict_hori = valider_horizontale(plateau, 5)
    dict_verti = valider_verticale(plateau, 5)
    for player in dict_diag:
        if len(dict_diag[player]) > 0:
            gagnant = player
        if len(dict_hori[player]) > 0:
            gagnant = player
        if len(dict_verti[player]) > 0:
            gagnant = player
    
    return gagnant
plateau_fini = [
        ["X", "X", "X", " ", " "],
        [" ", "X", " ", "X", " "],
        ["O", " ", "X", "O", "O"],
        [" ", "X", " ", "X", " "],
        [" ", "X", " ", " ", " "],
    ]
print(partie_terminée(plateau_fini))

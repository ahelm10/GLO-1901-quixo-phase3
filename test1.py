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
plateau = [
        [" ", "X", "X", " ", "X"],
        ["X", "X", "X", " ", " "],
        [" ", " ", "X", " ", "O"],
        ["X", "X", " ", "X", "X"],
        [" ", " ", " ", " ", " "],
    ]
print(valider_horizontale(plateau, 3))
    
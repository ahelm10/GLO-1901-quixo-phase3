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
        compteur_X = 0
        compteur_O = 0
        liste_X = []
        liste_O = []
        diagonale = []
        cord_x_debut = []
        cord_x_fin = []
        cord_o_debut = []
        cord_o_fin = []
        coord_x = []
        coord_o = []
        for i in range(len(plateau)):
            diagonale.append(plateau[i][i])
            if (plateau[i][i]).upper() == 'X':
                compteur_X += 1
                liste_X.append((i+1, i+1))
            elif(plateau[i][i]).upper() == 'O':
                compteur_O += 1
                liste_O.append((i+1, i+1))
        if compteur_X == nb_pions:
            cord_x_debut.append([str(diagonale.index('X')+1), str(diagonale.index('X')+1)])
            diagonale.reverse()
            cord_x_fin.append([str(len(plateau)-diagonale.index('X')), str(len(plateau)-diagonale.index('X'))])
            diagonale.reverse()
            coord_x = [cord_x_debut,cord_x_fin]
        if compteur_O == nb_pions:
            cord_o_debut.append([str(diagonale.index('O')+1), str(diagonale.index('O')+1)])
            diagonale.reverse()
            cord_o_fin.append([str(len(plateau)-diagonale.index('O')), str(len(plateau)-diagonale.index('O'))])
            coord_o = [cord_o_debut,cord_o_fin]

        resultat = {"X": coord_x , "O": coord_o}
        return resultat
plateau = [
        [" ", " ", " ", " ", "o"],
        [" ", "X", " ", " ", " "],
        [" ", " ", "X", " ", " "],
        [" ", " ", " ", "X", " "],
        [" ", " ", " ", "O", " "],
    ]
print(valider_diagonale(plateau, 3))
    
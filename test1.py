from plateau import *
import QuixoError

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
    plateau = Plateau(plateau_input)
    plateau.insertion('O', [5, 5], 'bas')
    print(plateau)

#test_insertion()
#test_creation()

def valider_diagonale(plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        liste_X = []
        liste_O = []
        for i in range(len(plateau)):
            if (plateau[i][i]).upper() == 'X':
                compteur_X += 1
            if compteur_X == nb_pions:
                 liste_X.append([(, )])
            if (plateau[i][i]).upper() == 'O':
                compteur_0 += 1

        resultat = {'X': liste_X, 'O': liste_O}
        return resultat
plateau = [
        [" ", " ", " ", " ", "o"],
        [" ", "X", " ", " ", " "],
        [" ", " ", "X", " ", " "],
        [" ", " ", " ", "X", " "],
        [" ", " ", " ", "O", " "],
    ]
print(valider_diagonale(plateau, 3))

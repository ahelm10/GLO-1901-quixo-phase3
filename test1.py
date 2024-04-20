from plateau import *

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
test_creation()



from copy import deepcopy

from quixo_error import QuixoError
class Plateau:
    """Module Plateau

    Classes:
        * Plateau - Classe principale du plateau de jeu Quixo.
    """
    def __init__(self, plateau=None):
        """Constructeur de la classe Plateau

        Vous ne devez rien modifier dans cette méthode.

        Args:
            plateau (list[list[str]], optional): La représentation du plateau
                tel que retourné par le serveur de jeu ou la valeur None par défaut.
        """
        self.plateau = self.construire_plateau(deepcopy(plateau))


    def état_plateau(self):
        """Retourne une copie du plateau

        Retourne une copie du plateau pour éviter les effets de bord.
        Vous ne devez rien modifier dans cette méthode.

        Returns:
            list[list[str]]: La représentation du plateau
            tel que retourné par le serveur de jeu.
        """
        return deepcopy(self.plateau)

    def __str__(self):
        """Retourne une représentation en chaîne de caractères du plateau

        Déplacer le code de votre fonction formater_plateau ici et ajuster le en conséquence.

        Returns:
            str: Une représentation en chaîne de caractères du plateau.
        """
        plateau = self.plateau
        row = 0
        col = 0
        plateau_str = "   -------------------\n"
        for ligne in plateau:
            plateau_str += str(row + 1)
            col = 0
            for case in ligne:
                plateau_str += " | " + plateau[row][col]
                col += 1
            if row < 4:
                plateau_str += " |\n" + "  |---|---|---|---|---|\n"
            else:
                plateau_str += " |\n" + "--|---|---|---|---|---\n"
            row += 1
        plateau_str += "  | 1   2   3   4   5\n"
        return plateau_str

    def __getitem__(self, position):
        """Retourne la valeur à la position donnée

        Args:
            position (tuple[int, int]): La position (x, y) du pion sur le plateau.

        Returns:
            str: La valeur à la position donnée, soit "X", "O" ou " ".

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
        """
        x, y = position
        if not (1 <= x <= 5 and 1 <= y <= 5):
            raise QuixoError("Les positions x et y doivent être entre 1 et 5 inclusivement.")
        return self.plateau[x-1][y-1]

    def __setitem__(self, position, valeur):
        """Modifie la valeur à la position donnée

        Args:
            position (tuple[int, int]): La position (x, y) du pion sur le plateau.
            value (str): La valeur à insérer à la position donnée, soit "X", "O" ou " ".

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
            QuixoError: La valeur donnée doit être "X", "O" ou " ".
        """
        x, y = position
        if not (1 <= x <= 5 and 1 <= y <= 5):
            raise QuixoError("Les positions x et y doivent être entre 1 et 5 inclusivement.")
        if valeur not in ["X", "O", " "]:
            raise QuixoError('La valeur donnée doit être "X", "O" ou " ".')
        self.plateau[x-1][y-1] = valeur.upper()

    def construire_plateau(self, plateau):
        """Construit un plateau de jeu

        Si un plateau est fourni, il est retourné tel quel.
        Sinon, si la valeur est None, un plateau vide de 5x5 est retourné.

        Args:
            plateau (list[list[str]] | None): La représentation du plateau
                tel que retourné par le serveur de jeu ou la valeur None.

        Returns:
            list[list[str]]: La représentation du plateau
                tel que retourné par le serveur de jeu.

        Raises:
            QuixoError: Le plateau doit être une liste de 5 listes de 5 éléments.
            QuixoError: Les éléments du plateau doivent être "X", "O" ou " ".
        """
        if plateau is not None:
            total = 0
            for ligne in plateau:
                for valeur in ligne:
                    total += 1
                    if valeur.upper() not in [" ", "X", "O"]:
                        raise QuixoError('Les éléments du plateau doivent être \"X\", \"O\" ou \" \".')
            if total != 25:
                raise QuixoError("Le plateau doit être une liste de 5 listes de 5 éléments.")
            return plateau
        plateau_vide = [
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " "],
                        ]
        return plateau_vide


    def insertion(self, pion, destination, direction):
        """Insère un pion dans le plateau

        Cette méthode appelle la méthode d'insertion appropriée selon la direction donnée.

        À noter que la validation des positions sont faites dans
        les méthodes __setitem__ et __getitem__. Vous devez donc en faire usage dans
        les diverses méthodes d'insertion pour vous assurez que les positions sont valides.

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            destination (list[int]): La position [x, y] où insérer le pion.
            direction (str): La direction de l'insertion, soit "haut", "bas", "gauche" ou "droite".

        Raises:
            QuixoError: La direction doit être "haut", "bas", "gauche" ou "droite".
            QuixoError: Le pion à insérer doit être "X" ou "O".
        """
        if pion not in ["X", "O"]:
            raise QuixoError("Le pion à insérer doit être 'X' ou 'O'.")
        if direction == "haut":
            self.insertion_par_le_haut(pion, destination)
        elif direction == "bas":
            self.insertion_par_le_bas(pion, destination)
        elif direction == "gauche":
            self.insertion_par_la_gauche(pion, destination)
        elif direction == "droite":
            self.insertion_par_la_droite(pion, destination)
        else:
            raise QuixoError("La direction doit être 'haut', 'bas', 'gauche' ou 'droite'.")

    def insertion_par_le_bas(self, pion, destination):
        """Insère un pion dans le plateau en direction du bas

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            destination (list[int]): La position [x, y] où insérer le pion.

        Raises:
            QuixoError: La destination doit avoir une position y de 5.
        """
        x, y = destination
        if y != 5:
            raise QuixoError("La destination doit avoir une position y de 5.")
        x = x-1
        y = y-1
        for i in range(4):
            self.plateau[i][y] = self.plateau[i+1][y]
        self.plateau[4][y] = pion
    def insertion_par_le_haut(self, pion, destination):
        """Insère un pion dans le plateau en direction du haut

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            destination (list[int]): La position [x, y] où insérer le pion.

        Raises:
            QuixoError: La destination doit avoir une position y de 1.
        """
        x, y = destination
        if y != 1:
            raise QuixoError("La destination doit avoir une position y de 1.")
        x = x-1
        y = y-1
        for i in range(4,0,-1):
            self.plateau[i][y] = self.plateau[i-1][y]
        self.plateau[0][y] = pion

    def insertion_par_la_gauche(self, pion, destination):
        """Insère un pion dans le plateau en direction de la gauche

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            destination (list[int]): La position [x, y] où insérer le pion.

        Raises:
            QuixoError: La destination doit avoir une position x de 1.
        """
        x, y = destination
        if x != 1:
            raise QuixoError("La destination doit avoir une position x de 1.")
        x = x-1
        y = y-1
        for i in range(4,0,-1):
            self.plateau[x][i] = self.plateau[x][i-1]
        self.plateau[x][0] = pion

    def insertion_par_la_droite(self, pion, destination):
        """Insère un pion dans le plateau en direction de la droite

        Args:
            pion (str): La valeur du pion à insérer, soit "X" ou "O".
            destination (list[int]): La position [x, y] où insérer le pion.

        Raises:
            QuixoError: La destination doit avoir une position x de 5.
        """
        x, y = destination
        if x != 5:
            raise QuixoError("La destination doit avoir une position x de 5.")
        x = x-1
        y = y-1
        for i in range(0,4):
            self.plateau[x][i] = self.plateau[x][i+1]
        self.plateau[x][4] = pion

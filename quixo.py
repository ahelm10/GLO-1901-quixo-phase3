"""Module Quixo

Classes:
    * Quixo - Classe principale du jeu Quixo.
    * QuixoError - Classe d'erreur pour le jeu Quixo.

Functions:
    * analyser_commande - Génère un interpréteur de commande.
    * formater_les_parties - Formater la liste des dernières parties.
"""
import argparse

from plateau import Plateau
from quixo_error import QuixoError


class Quixo:
    def __init__(self, joueurs, plateau=None) -> None:
        """Constructeur de la classe Quixo

        Vous ne devez rien modifier dans cette méthode.

        Args:
            joueurs (list[str]): La liste des deux joueurs.
                Le premier joueur possède le symbole "X" et le deuxième "O".
            plateau (list[list[str]], optional): La représentation du plateau
                tel que retourné par le serveur de jeu ou la valeur None par défaut.
        """
        self.joueurs = joueurs
        self.plateau = Plateau(plateau)

    def état_partie(self):
        """Retourne une copie du jeu

        Retourne une copie du jeu pour éviter les effets de bord.
        Vous ne devez rien modifier dans cette méthode.

        Returns:
            dict: La représentation du jeu tel que retourné par le serveur de jeu.
        """
        return {
            "joueurs": self.joueurs,
            "plateau": self.plateau.état_plateau(),
        }

    def __str__(self):
        """Retourne une représentation en chaîne de caractères de la partie

        Déplacer le code de vos fonctions formater_légende et formater_jeu ici.
        Adaptez votre code en conséquence et faites appel à Plateau
        pour obtenir la représentation du plateau.

        Returns:
            str: Une représentation en chaîne de caractères du plateau.
        """
        legende = "Légende: X=" + self.joueurs[0] + ", O = " + self.joueurs[1] + "\n"
        plateau = str(self.plateau)
        return legende + plateau
    def déplacer_pion(self, pion, origine, direction):
        """Déplacer un pion dans une direction donnée.

        Applique le changement au Plateau de jeu

        Args:
            pion (str): Le pion à déplacer, soit "X" ou "O".
            origine (list[int]): La position (x, y) du pion sur le plateau.
            direction (str): La direction du déplacement, soit "haut", "bas", "gauche" ou "droite".
        """
        self.plateau.insertion(pion, origine, direction)

    def récupérer_le_coup(self):
        """Demander le prochain coup à jouer au joueur.

        Déplacer le code de votre fonction récupérer_le_coup ici et ajuster le en conséquence.
        Vous devez maintenant valider les entrées de l'utilisateur.

        Returns:
            tuple: Tuple de 2 éléments composé de l'origine du bloc à déplacer et de sa direction.
                L'origine est une liste de 2 entiers [x, y].
                La direction est une chaîne de caractères.

        Raises:
            QuixoError: Les positions x et y doivent être entre 1 et 5 inclusivement.
            QuixoError: La direction doit être "haut", "bas", "gauche" ou "droite".

        Examples:
            Donnez la position d'origine du bloc (x,y) :
            Quelle direction voulez-vous insérer? ('haut', 'bas', 'gauche', 'droite') :
        """
        x, y = map(int, input(
            "Donnez la position d'origine du bloc (x,y), séparés par une virgule: ").split(','))
        if not (1 <= x <= 5 and 1 <= y <= 5):
            raise QuixoError("Position invalide. Les coordonnées doivent être comprises entre 1 et 5.")

        direction = input(
            "Quelle direction voulez-vous insérer? ('haut', 'bas', 'gauche', 'droite'): ").strip().lower()
        if direction not in ['haut', 'bas', 'gauche', 'droite']:
            raise QuixoError("Direction invalide. Veuillez choisir parmi 'haut', 'bas', 'gauche', 'droite'.")
        return ([x, y], direction)
def analyser_commande():
    """Génère un interpréteur de commande.
    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
            Cet objet aura l'attribut «idul» représentant l'idul du joueur
            et l'attribut «parties» qui est un booléen True/False.
    """
    parser = argparse.ArgumentParser()
    parser.description = 'Quixo'
    parser.add_argument('idul', type=str, help="IDUL du joueur", default='')
    parser.add_argument('-p', '--parties', dest='parties', action='store_true',
                         help="Lister les parties existantes", default = False)
    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()


def formater_les_parties(parties):
    """Formater la liste des dernières parties.

    L'ordre doit rester exactement le même que ce qui est passé en paramètre.

    Args:
        parties (list): Liste des parties

    Returns:
        str: Représentation des parties
    """
    index = 0
    texte = ""
    for p in parties:
        gagnant  = p.get("gagnant")
        index += 1
        if gagnant is None:
            texte += str(index) + " : " + p.get("date") + ", " +  p.get(
                "joueurs")[0] + " vs " +  p.get("joueurs")[1] + "\n"
        else:
            texte += str(index) + " : " + p.get("date") + ", " +  p.get(
                "joueurs")[0] + " vs " +  p.get("joueurs")[1] + ", gagnant: " + gagnant + "\n"
    return texte

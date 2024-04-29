from quixo import Quixo
import QuixoError


class QuixoIA(Quixo):
    def __init__(self):
        super().__init__()
    
    def valider_diagonale(self, plateau, nb_pions=5):
        if nb_pions < 3 or nb_pions > 5:
            raise QuixoError("Le nombre de pions doit être entre 3 et 5.")
        compteur_X = compteur_X = 0
        liste_X = []
        liste_O = []
        diagonale = []
        for i in range(len(plateau)):
            diagonale.append(plateau[i][i])
            if (plateau[i][i]).upper() == 'X':
                compteur_X += 1
                liste_X.append((i+1, i+1))
            elif(plateau[i][i]).upper() == 'O':
                compteur_0 += 1
                liste_O.append((i+1, i+1))

        resultat = {'X': liste_X, 'O': liste_O}
        return resultat
    
    def valider_horizontale(self, plateau, nb_pions=5):
        for y in range(len(plateau)):
            ligne = [plateau[y][x] for x in range(len(plateau[y]))]
            if self.valider_ligne(ligne, 'X', nb_pions):
                return {'X': [(y, x) for x in range(len(ligne)) if ligne[x] == 'X']}
            elif self.valider_ligne(ligne, 'O', nb_pions):
                return {'O': [(y, x) for x in range(len(ligne)) if ligne[x] == 'O']}
        return {}

    def valider_verticale(self, plateau, nb_pions=5):
        for x in range(len(plateau[0])):
            colonne = [plateau[y][x] for y in range(len(plateau))]
            if self.valider_ligne(colonne, 'X', nb_pions):
                return {'X': [(y, x) for y in range(len(colonne)) if colonne[y] == 'X']}
            elif self.valider_ligne(colonne, 'O', nb_pions):
                return {'O': [(y, x) for y in range(len(colonne)) if colonne[y] == 'O']}
        return {}

    def partie_terminée(self):
        for f in [self.valider_horizontale, self.valider_verticale, self.valider_diagonale]:
            for pion in ['X', 'O']:
                if f(self.plateau, pion=pion):
                    return pion
        return None

    def trouver_coup_gagnant(self, pion):
    
    def trouver_coup_bloquant(self, pion):
        

    def jouer_le_coup(self, pion):
        if self.partie_terminée():
            raise QuixoError("La partie est déjà terminée.")

        coup_gagnant = self.trouver_coup_gagnant(pion)
        if coup_gagnant:
            return coup_gagnant

        coup_bloquant = self.trouver_coup_bloquant(pion)
        if coup_bloquant:
            return coup_bloquant
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
    
    def pions_jouables(self, plateau, pion):
        jouables  = []
        plateau_copie = plateau.état_plateau()
        for i in range(len(plateau_copie)):
            for j in range(len(plateau_copie)):
                if (plateau_copie[i][j]).upper() in [pion.upper(), ' '] and (i in [0, 4] or j in [0, 4]):
                    jouables.append((i+1,j+1))
        return jouables
    
    def coups_jouables(self,plateau, pion):
        jouables  = []
        directions  = ["haut", "bas", "gauche", "droite"]
        plateau_copie = plateau.état_plateau()
        for coord in self.pions_jouables(plateau_copie, pion):
            x,y = coord
            for direction in directions:
                jouables.append(([x, y], direction))
        return jouables

    def simuler_deplacement(self, pion_coord, coup, plateau):
        plateau_temp = [row[:] for row in plateau]
        x, y = pion_coord
        coup_x, coup_y = coup
        plateau_temp[coup_x][coup_y] = plateau_temp[x][y]
        plateau_temp[x][y] = ' '
        return plateau_temp

    def est_coup_gagnant(self, plateau, coup, pion):
        x, y = coup
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        
        def compte_pions(dx, dy):
            count = 1
            for step in range(1, 5):
                nx, ny = x + step * dx, y + step * dy
                if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[0]) and plateau[nx][ny] == pion:
                    count += 1
                else:
                    break
            for step in range(1, 5):
                nx, ny = x - step * dx, y - step * dy
                if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[0]) and plateau[nx][ny] == pion:
                    count += 1
                else:
                    break
            return count >= 5

        for dx, dy in directions:
            if compte_pions(dx, dy):
                return True
        return False

    def trouver_coup_gagnant(self, pion):
        pions_jouables = self.pions_jouables(self.plateau, pion)
        for pion_coord in pions_jouables:
            coups = self.coups_jouables(self.plateau, pion, pion_coord)
            for coup, direction in coups:
                plateau_temp = self.simuler_deplacement(pion_coord, coup, self.plateau)
                if self.est_coup_gagnant(plateau_temp, coup, pion):
                    return pion_coord, direction

        raise QuixoError("Aucun coup gagnant possible.")
    
    def trouver_coup_bloquant(self, pion):
        plateau = self.plateau
        adversaire = 'O' if pion == 'X' else 'X'
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]  
        
        for x in range(len(plateau)):
            for y in range(len(plateau[x])):
                if plateau[x][y].upper() == adversaire:
                    for dx, dy in directions:
                        compte = 1
                        for step in range(1, 4):
                            nx, ny = x + dx * step, y + dy * step
                            if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[nx]) and plateau[nx][ny].upper() == adversaire:
                                compte += 1
                            else:
                                break
                        if compte == 4:
                            for step in range(5):
                                nx, ny = x + dx * step, y + dy * step
                                if 0 <= nx < len(plateau) and 0 <= ny < len(plateau[nx]) and plateau[nx][ny] == ' ':
                                    if (nx == 0 or nx == len(plateau)-1 or ny == 0 or ny == len(plateau[nx])-1):
                                        return (nx, ny), 'haut' if dy == -1 else 'bas' if dy == 1 else 'gauche' if dx == -1 else 'droite'
        raise QuixoError("Aucun coup bloquant possible.")
    
    import random
    
    
    def jouer_le_coup(self, pion):
        if self.partie_terminee():
            raise QuixoError("La partie déjà est terminée.")
        
        try:
            coup_gagnant = self.trouver_coup_gagnant(pion)
            if coup_gagnant:
                self.deplacer_pion(coup_gagnant[0], coup_gagnant[1], self.plateau)
                return coup_gagnant
            coup_bloquant = self.trouver_coup_bloquant(pion)
            if coup_bloquant:
                self.deplacer_pion(coup_bloquant[0], coup_bloquant[1], self.plateau)
                return coup_bloquant
        except QuixoError:
            coups_jouables = self.coups_jouables(self.plateau, pion)
            if not coups_jouables:
                raise QuixoError("Aucun coup n'est possible.")
            
            coup_aleatoire = random.choice(coups_jouables)
            self.deplacer_pion(coup_aleatoire[0], coup_aleatoire[1], self.plateau)
            return coup_aleatoire
    
    import argparse

    def parse_arguments():
        parser = argparse.ArgumentParser(description="Jouer au Quixo contre l'ordinateur")
        parser.add_argument('idul', type=str, help='IDUL du joueur')
        parser.add_argument('-p', '--parties', action='store_true', help='Lister les parties existantes')
        parser.add_argument('-a', '--automatique', action='store_true', help='Jouer automatiquement')
        
        return parser.parse_args()

    def main():
        args = parse_arguments()
        
        if args.parties:
            lister_parties()
        elif args.automatique:
            jouer_automatiquement(args.idul)
        else:
            print("Aucune option spécifique choisie, lancement du jeu en mode manuel.")
            jouer_manuellement(args.idul)

    def lister_parties():
        print("Listing des parties existantes...")

    def jouer_manuellement(idul):
        print(f"Démarrage du jeu manuel pour {idul}...")
        
    def jouer_automatiquement(idul):
        print(f"Initialisation du jeu pour {idul} en mode automatique...")
        jeu = Quixo(idul)  
        jeu.initialiser_plateau()
        
        while not jeu.partie_terminee():
            coup = jeu.jouer_le_coup()
            jeu.afficher_plateau()
            if jeu.verifier_gagnant():
                print(f"Le gagnant est {jeu.gagnant()}")
                break
        
        print("Fin du jeu")
        jeu.afficher_resultats_finaux()

    if __name__ == '__main__':
        main()
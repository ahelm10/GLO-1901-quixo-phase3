class QuixoError(Exception):
    """Module QuixoError

    Classes:
        * QuixoError - Classe d'erreur pour le jeu Quixo.
    """
    def __init__(self, message="Une erreur est apparue"):
        self.message = message
        super().__init__(self.message)

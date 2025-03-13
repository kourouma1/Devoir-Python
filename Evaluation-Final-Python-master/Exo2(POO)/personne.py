import random

class Personne:
    def __init__(self, nom, sante='saine', proba_infection=0.1):
        """
        Initialise une personne. """
        self.nom = nom
        self.sante = sante
        self.proba_infection = proba_infection

    def est_infectee(self):
        """
        Vérifie si la personne est infectée.
        """
        return self.sante == 'infectée'

    def contaminer(self):
        """
        Infecte la personne avec une  probabilité.
        """
        if self.sante == 'saine' and random.random() < self.proba_infection:
            self.sante = 'infectée'

    def guerir(self, proba_guerison=0.05):
        """
        Immunise la personne si elle était infectée, avec une  probabilité. """
        if self.sante == 'infectée' and random.random() < proba_guerison:
            self.sante = 'immunisée'

    def __str__(self):
        """
        Représentation  de la personne.
        """
        return f"{self.nom} ({self.sante})"

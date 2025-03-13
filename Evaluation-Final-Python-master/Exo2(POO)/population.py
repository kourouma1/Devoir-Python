
class Population:
    def __init__(self):
        """
        Initialise une population vide.
        """
        self.individus = []

    def ajouter_personne(self, personne):
       
        self.individus.append(personne)

    def propager_maladie(self):
        """
        methode pour la propagation de la maladie dans la population.
        """
        # Liste des personnes infectées
        infectes = [p for p in self.individus if p.est_infectee()]

        # Pour chaque personne saine, vérifier si elle est contaminée par un contact
        for personne in self.individus:
            if personne.sante == 'saine' and infectes:
                personne.contaminer()

    def afficher_statistiques(self):
        """
        Affiche les statistiques de la population.
        """
        sains = sum(1 for p in self.individus if p.sante == 'saine')
        infectes = sum(1 for p in self.individus if p.est_infectee())
        immunises = sum(1 for p in self.individus if p.sante == 'immunisée')

        print(f"Statistiques de la population :")
        print(f"- Sains : {sains}")
        print(f"- Infectés : {infectes}")
        print(f"- Immunisés : {immunises}")
        print()

    def __str__(self):
        """
        Représentation  de la population.
        """
        return "\n".join(str(p) for p in self.individus)

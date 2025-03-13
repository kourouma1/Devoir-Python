import random
from population import Population
from personne import Personne


if __name__ == "__main__":
    # Créer une population de 1000 personnes
    population = Population()
    for i in range(1, 1001):
        population.ajouter_personne(Personne(f"Personne {i}", sante='saine', proba_infection=0.1))

    # Introduire 10 personnes infectées au hasard
    infectes_initiaux = random.sample(population.individus, 10)
    for personne in infectes_initiaux:
        personne.sante = 'infectée'

    # Simuler 30 jours de propagation
    for jour in range(1, 31):
        print(f"=== Jour {jour} ===")
        population.propager_maladie()

        # Guérir certaines personnes infectées
        for personne in population.individus:
            personne.guerir(proba_guerison=0.05)

        # Afficher les statistiques de la population
        population.afficher_statistiques()
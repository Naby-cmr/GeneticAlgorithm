import random
import string
from AbstractClasses import *

target = "Ceci est un algorithme genetique solvant un probleme d'optimisation."


class DNA(AbstractDNA):
    """Classe ADN."""

    def __init__(self, genes=None):
        """Constructeur."""
        super().__init__()
        self._genes = genes or self.make_genes(string.printable)

    # Abstract method
    def make_genes(self, l):
        """Construit des gènes."""
        seq = random.choices(list(l), k=len(target))
        return "".join(seq)

    # Abstract method
    def mutate(self, rate):
        """Fonction de mutation."""
        rand = random.randint(0, 100)
        if rand <= 100*rate:
            i = random.randint(0, len(self._genes)-1)
            self._genes = self._genes[:i] + random.choice(string.printable)[0]\
                                          + self._genes[i+1:]

    # Abstract method
    def crossover(self, other):
        """Fonction de reproduction."""
        i = random.randint(0, len(self._genes))
        return self._genes[0:i] + other._genes[i:]


class Individual(AbstractIndividual):
    """Classe Individu."""

    def __init__(self, dna=None):
        """Constructeur."""
        super().__init__()
        self._fitness = 0
        self._DNA = dna or DNA()

    # Abstract method
    def computeFitness(self, target):
        """Fonction de fitness."""
        cpt = 0
        for i, j in zip(self.get_DNA().get_genes(), target):
            if i == j:
                cpt += 1
        self._fitness = cpt/len(target)
        return self._fitness


class Population(AbstractPopulation):
    """Classe Population."""

    def __init__(self, n):
        """Constructeur."""
        self.individuals = [Individual() for i in range(n)]
        self.size = n
        self.max_fitness = 0

    # Abstract method
    def stopIteration(self, n=None):
        """Critere d'arrêt de l'évolution."""
        if self.max_fitness >= 1.0:
            return True
        else:
            return False

    # Abstract method
    def createDNA(self, genes):
        """Retourne un objet DNA."""
        return DNA(genes)

    # Abstract method
    def createIndividual(self, dna):
        """Retourne un objet individu."""
        return Individual(dna)

    # Abstract method
    def trackingProcess(self, best, n):
        """Suivi du process d'évolution."""
        print(f"{str(best.get_DNA().get_genes()).encode('unicode_escape').decode()} | \
        Fitness: {best.get_fitness()} | Generation: {n}                         \r", end="")


def main():
    """Start function."""
    size = 500
    selection = 0.5
    mutation = 0.1
    population = Population(size)
    population.evolve(selection, mutation, target)


if __name__ == "__main__":
    main()

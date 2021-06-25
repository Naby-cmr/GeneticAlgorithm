from abc import ABC, abstractmethod
import random

__all__ = ['AbstractDNA', 'AbstractIndividual', 'AbstractPopulation']


class AbstractDNA(ABC):
    """Classe abstraite d'ADN."""

    def __init__(self):
        """Constructeur."""
        self._genes = None

    def __str__(self):
        """Pretty-print."""
        return str(self._genes)

    def get_genes(self):
        """Getter."""
        return self._genes

    @abstractmethod
    def make_genes(self, *args):
        """Fonction de création des gènes."""
        pass

    @abstractmethod
    def mutate(self, rate):
        """Fonction de mutation."""
        pass

    @abstractmethod
    def crossover(self, mate):
        """Fonction de reproduction."""
        pass


class AbstractIndividual(ABC):
    """Classe abstraite d'individu."""

    def __init__(self):
        """Constructeur."""
        self._fitness = 0
        self._DNA = None

    def __lt__(self, other):
        """Surcharge opérateur de comparaison."""
        return self._fitness < other.get_fitness()

    def __str__(self):
        """Pretty-print."""
        return f"""
            Fitness : {self._fitness}
            DNA : {self.get_DNA()}
        """

    def get_DNA(self):
        """Getter."""
        return self._DNA

    @abstractmethod
    def computeFitness(self, *args):
        """Fonction de fitness."""
        pass

    def get_fitness(self):
        """Getter."""
        return self._fitness


class AbstractPopulation(ABC):
    """Classe abstraite de population."""

    def __init__(self):
        """Constructeur."""
        self.individuals = list()
        self.size = 0
        self.max_fitness = 0

    def __str__(self):
        """Pretty-print."""
        for ind in self.individuals:
            print(f"Individual {self.individuals.index(ind)}")
            print(ind)
        return f"""
        Size of population : {len(self.individuals)}
        Maximum fitness : {self.max_fitness}
        """

    @abstractmethod
    def createDNA(self, *args):
        """Retourne un objet DNA."""
        pass

    @abstractmethod
    def createIndividual(self, *args):
        """Retourne un objet individu."""
        pass

    def computeFitness(self, *args):
        """Fonction de fitness."""
        for ind in self.individuals:
            max_fitness = ind.computeFitness(*args)
            if max_fitness > self.max_fitness:
                self.max_fitness = max_fitness

    def select(self, rate):
        """Fonction de sélection des meilleurs individus."""
        self.individuals.sort(reverse=True)
        self.individuals = self.individuals[0:int((rate)*self.size)]
        return self.individuals[0]

    def reproduce(self, m):
        """Fonction de reproduction."""
        # print('caca')
        childrens = []
        random.shuffle(self.individuals)
        while self.size != len(childrens):
            for i in range(0, len(self.individuals)-1, 2):
                dna1 = self.individuals[i].get_DNA()
                dna2 = self.individuals[i+1].get_DNA()
                childDNA = self.createDNA(dna1.crossover(dna2))
                # childDNA = DNA(mate1.crossover(mate2))
                childDNA.mutate(m)
                ind = self.createIndividual(childDNA)
                childrens.append(ind)
                # childrens.append(Individual(childDNA))
                if len(childrens) == self.size:
                    break
        self.individuals = childrens

    def stopIteration(self, n):
        """Critere d'arrêt de l'évolution."""
        pass

    def trackingProcess(self, best, n):
        """Suivi du process d'évolution."""
        pass

    def evolve(self, selection, mutation, target=None):
        """Suivi du process d'évolution."""
        n = 0
        while True:
            self.computeFitness(target)
            best = self.select(selection)
            self.trackingProcess(best, n)
            if self.stopIteration(n):
                print()
                break
            self.reproduce(mutation)
            n = n + 1

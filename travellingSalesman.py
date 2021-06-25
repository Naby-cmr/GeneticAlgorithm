from AbstractClasses import *
import random
import string
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import namedtuple
from math import hypot,sqrt,cos,sin,pi

Point = namedtuple('Point',['x','y','z'])
cities = []
for i in range(50):
    x = random.randint(0,800)
    x = 20*cos(2*pi*i/50)
    y = random.randint(0,600)
    y = 20*sin(2*pi*i/50)
    z = random.randint(0,100)
    point = Point._make((x,y,z))
    cities.append((i,point))

class DNA(AbstractDNA):
    def __init__(self, genes = None):
        self._genes = genes or self.make_genes()

    # Abstract method
    def make_genes(self):
        random.shuffle(cities)
        return list(cities)

    # Abstract method
    def mutate(self,rate):
        rand = random.randint(0,100)
        if rand < 100*rate:
            i = random.randint(0,len(self._genes)-1)
            j = random.randint(0,len(self._genes)-1)
            while (i==j):
                j = random.randint(0,len(self._genes)-1)
            self._genes[i],self._genes[j] = self._genes[j],self._genes[i]

    # Abstract method
    def crossover(self,other):
        start = random.randint(0,len(self._genes)-1)
        end = random.randint(0,len(self._genes)-1)

        i = min(start,end)
        j = max(start,end)

        pattern = self._genes[i:j]
        L = [i for i in other._genes if i not in pattern]
        L[i:i] = pattern
        self._genes = L
        return self._genes

    def distance(self,a:Point,b:Point):
        return hypot(b.x-a.x,b.y-a.y)

class Individual(AbstractIndividual):

    def __init__(self,dna=None):
        self._fitness = 0
        self._DNA = dna or DNA()
        # print(self._DNA)

    # Abstract method
    def computeFitness(self,args=None):
        route = self.get_DNA()
        cities = route.get_genes()
        for i in range(0,len(cities)-1):
            self._fitness = self._fitness + route.distance(cities[i][1],cities[i+1][1])
        self._fitness = self._fitness + route.distance(cities[-1][1],cities[0][1])
        self._fitness = 1.0/self._fitness
        return self._fitness

class Population(AbstractPopulation):

    def __init__(self,n):
        self.individuals = [self.createIndividual() for i in range(n)]
        self.size = n
        self.max_fitness = 0

    # Abstract method
    def createDNA(self,*args):
        return DNA(*args)

    # Abstract method
    def createIndividual(self,*args):
        return Individual(*args)

    # Abstract method
    def stopIteration(self,n=None):
        if n >= 1000:
            return True
        else:
            return False

    def trackingProcess(self,best,n):
        route = best.get_DNA().get_genes()
        points = [x[1] for x in route]
        x = [point.x for point in points]
        y = [point.y for point in points]

        plt.title(f"Fitness: {best.get_fitness()} | Generation: {n}")

        plt.plot(x,y,'ro')
        plt.plot(x,y,'b-')
        plt.plot([x[-1],x[0]],[y[-1],y[0]],'b-')
        plt.draw()
        plt.pause(0.0001)
        plt.clf()

size = 1000
selection = 0.5
mutation = 0.1
population = Population(size)
fig, ax = plt.subplots()
population.evolve(selection,mutation)

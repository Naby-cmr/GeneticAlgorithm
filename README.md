## Explanations

In Darwin’s evolution theory, a population of individuals follows natural selection : the surviving subjects of a population are the most adaptable to their environment. They are able to reproduce to conceive the next generation of individuals of the population which will be stronger due to a better genetic material. A genetic algorithm uses this idea by following a pattern in three steps for one generation of a population :

The selection phase : the strongest individuals of the population remain. A fitness function needs to be computed to be able to find the "fittest" subjects. Only a fraction of them is selected (selection rate). This simulates natural selection.

The crossover phase : two individuals from the previous step are chosen to conceive one child. Their genetic material is mixed according to a crossover function. This simulates reproduction.

The mutation phase : the genetic material of each child of the previous step can be altered through a mutation rate. This simulates gene mutation of DNA. This process repeats itself over a significant amount of iterations, each one representing a new generation. After a certain amount of generations, one can hope having an ultimate population composed of environment-resistant individuals. The algorithm stops when a criteria is met.


## How to proceed

The goal of the exercice is to use a genetic algorithm to find the content of a target sentence. 

The target sentence is "I use a genetic algorithm to solve an optimization problem"

The genes (genetical material) are the characters composing the sentence.

The fitness function returns the ratio of the number of the right characters at the right place in the sentence and the number of characters in the sentence.

The selection rate defines the n % of the fittest individuals that are kept for reproduction. The individuals reproduce by pair. The crossover function is designed such that the offspring get one part of the first parent’s genes and one part of the second parent’s
genes.

The mutation fonction randomly alters one gene (or character) of the child with a defined probability (mutation rate)


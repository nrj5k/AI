The N Queens Problem

Since I have 2 programs that implement the N Queens problem. I shall first
elaborate on it.

The N Queens problem is one where you have a chess board of NxN dimensions and
your aim is to put N Queens such that none of them are a "threat" to each other.
N is 4 and above.

So the N Queens problem was solved using 2 search algorithms.
1. Genetic Algorithms
2. Simulated Annealing

1. Genetic Algorithms

This method of solution finding similar to Evolution.

-> You have a randomly generated set of solutions, these start as your initial base,
then you compare their fitness.
Here for the N Queens Problem, the fitness function rewards a point when a Queen
does not "threaten" another Queen. So we check the first Queen with the rest, and
so on. Now the last Queen does not really threaten anyone, as we are considering
threats from the Left side of the board to the Right, and a "threat" is a bidirectional
"effect". So the last Queen is ignored and the maximum fitness it can achieve is
always N-1.

-> Once the fitness is checked the possible solutions, from now called Parents, need
to Reproduce/Crossover.
There are many ways to 'Reproduce' the parents. The one implemented here is a
simple One-point Crossover.
More details here https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)
The Parent selection is done based on the fitness of the parent. That does not
mean that unfit Parents will never Reproduce and the Fittest will always Reproduce
a weighted probability function picks them, so there is a preference to the more fit
entities and not as much to the less fit ones. This does not mean that the least
fit Parent will never be chosen. It does get picked sometimes.

-> After they Reproduce and have a Child, which is put into a new set with just
the children after each reproduction step, based on a certain probability factor
a small Mutation occurs. In simple terms Mutation is simply changing a value randomly
of the child. This Mutation ensures that more of the search space is searched and
it ensures that the solution does not reach a local maxima.
https://www.quora.com/On-a-graph-whats-the-difference-between-global-and-local-maximum-minimum-values
So Mutation is good!
There are many ways to perform Mutation.
Check out https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm) for more info.
Here the positions are swapped, as it ensures a higher rate of fitness.

-> Once the number of children reach a certain size, it replaces the parent and
the process it either repeated M times, a preconfigured number, or till it finds
solution using the fitness function.

This method eventually finds the answer but the time it takes increases once the
value is more than 10. I have got the answers for N=19 and all but not always. You
gotta get lucky.

2. Simulated Annealing

Simulated Annealing is a search technique inspired by metallurgy, which involves
heating and controlled cooling of a material.
Now each step involves one a move, one move ie. one move of the Queen, or swapping
its position with another Queen.

It uses a fitness function similar to the one used in GA solution.

It starts off with a randomly generated solution and then makes a move.

The does not discard a a less fit solution. The probability of it picking a less fit
solution depends on the temperature and the change in energy. In general, the higher
the temperature the higher the chances of a less fit solution being accepted.
Check out http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/
for some cool functions for the cooling function.

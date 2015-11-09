Artificial intelligence
=======================

These are some programs/scripts I have implemented as part of my AI course and more.

1. N Queens Problem, Genetic Algorithms and Simulated Annealing
2. Monte Carlo Simulation for Blackjack

## The N Queens Problem
Since I have 2 programs that implement the N Queens problem. I shall first elaborate on it.

The N Queens problem is one where you have a chess board of NxN dimensions and your aim is to put N Queens such that none of them are a "threat" to each other. N is 4 and above.

So the N Queens problem was solved using 2 search algorithms. 

1. Genetic Algorithms 
2. Simulated Annealing

###1. Genetic Algorithms

  This method of solution finding similar to Evolution.
  - You have a randomly generated set of solutions, these start as your initial base, then you compare their fitness. Here for the N Queens Problem, the fitness function rewards a point when a Queen does not "threaten" another Queen. So we check the first Queen with the rest, and so on. Now the last Queen does not really threaten anyone, as we are considering threats from the Left side of the board to the Right, and a "threat" is a bidirectional "effect". So the last Queen is ignored and the maximum fitness it can achieve is always N-1.

  - Once the fitness is checked the possible solutions, from now called Parents, need to Reproduce/Crossover. There are many ways to 'Reproduce' the parents. The one implemented here is a simple One-point Crossover. More details [here](https://en.wikipedia.org/wiki/Crossover_(genetic_algorithm)) The Parent selection is done based on the fitness of the parent. That does not mean that unfit Parents will never Reproduce and the Fittest will always Reproduce a weighted probability function picks them, so there is a preference to the more fit entities and not as much to the less fit ones. This does not mean that the least fit Parent will never be chosen. It does get picked sometimes.

  - After they Reproduce and have a Child, which is put into a new set with just the children after each reproduction step, based on a certain probability factor a small Mutation occurs. In simple terms Mutation is simply changing a value randomly of the child. This Mutation ensures that more of the search space is searched and it ensures that the solution does not reach a local maxima. Some more info [here](https://www.quora.com/On-a-graph-whats-the-difference-between-global-and-local-maximum-minimum-values) So Mutation is good! There are many ways to perform Mutation. Check out [this wiki page](https://en.wikipedia.org/wiki/Mutation_(genetic_algorithm)) for more info. Here the positions are swapped, as it ensures a higher rate of fitness.

  - Once the number of children reach a certain size, it replaces the parent and the process it either repeated M times, a preconfigured number, or till it finds solution using the fitness function.

  This method eventually finds the answer but the time it takes increases once the value is more than 10. I have got the answers for N=19 and all but not always. You gotta get lucky.

###2. Simulated Annealing

*  Simulated Annealing is a search technique inspired by metallurgy, which involves heating and controlled cooling of a material. Now each step involves one a move, one move ie. one move of the Queen, or swapping its position with another Queen.

*  It uses a fitness function similar to the one used in GA solution. It starts off with a randomly generated solution and then makes a move.

*  This method does not discard a a less fit solution. The probability of it picking a less fit solution depends on the temperature and the change in energy. In general, the higher the temperature the higher the chances of a less fit solution being accepted. Check [this out](http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/) for some cool functions for the cooling function.

## The Monte Carlo Simulation
The Monte Carlo Simulation is a mathematical technique that allows quantitative analysis for decision making. In simple terms, to find a possible solution, you find the possible outcomes for a subset of the problem and that should give you a fair idea what the possible outcome can be.

#### Blackjack

I do not think this game needs an explanation but if you don't know the game [the wiki page](https://en.wikipedia.org/wiki/Blackjack) covers the basics.

#### The Implementation

* The simulation takes into account the varied values of Ace ( 1 or 11). It does not split. It kind plays like an amateur who knows the basics and has an idea of  the game.

* The dealer holds at 17 or above. The player only holds at 20 or above (ie Blackjack)

* If either the dealer or player gets more than 21, the total is reacalculated by converting an Ace, if present, from 11 to 1. If it's still more than 21 they go bust.

Check out the [outcomes](https://github.com/nrj5k/AI/blob/master/monte_carlo_blackjack_sim_outcome) to see different game simulations and outcomes. It runs a 1000 simulations and gives the probability of the player winning, losing and drawing the game.

The odds are usually around
* Win%: 31.8 
* Lose%: 64.0 
* Draw%: 4.2

In general. Once again reinstating the fact that if you do not know how to gamble. *DONT!*

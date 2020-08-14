'''
The Knapsack Problem:
Suppose you are Indiana Jones, and you have found the secret entrance to the Temple of Doom.
Before you is a multitude of artifacts and treasures - pots, gemstones, works of art, and more.
These belong in a museum! But there are soldiers hot on your heels, and you can only carry so much...
You, brave explorer, are facing the knapsack problem - maximizing the value of a set of items
you select that are constrained by total size/weight. The size and the value of an item need not
be correlated - the most precious item may be a tiny gemstone. But it turns out it's pretty tricky
to get a truly optimal solution, and that a bruteforce approach really doesn't scale.

A bit more motivation - this is a very general optimization problem that can be applied in a multitude
of situations, from resource selection and allocation to stuffing stolen goods in knapsacks.

![xkcd "NP-Complete"](https://imgs.xkcd.com/comics/np_complete.png "General solutions get you a 50% tip.")

The specific goal of this exercise is to write a program that takes input files that look like this:
1 42 81
2 42 42
3 68 56
4 68 25
5 77 14
6 57 63
7 17 75
8 19 41
9 94 19
10 34 12
The first row number is just a row/observation number, to facilitate reading and referring to items.
The second number is the size/cost of the item, i.e. the cost of putting it in your knapsack.
The third number is the value, i.e. the utility/payoff you get for selecting that item. The program
should also take as input a total size, which can just be a number passed from the command line.
So execution may look like this: `python knapsack.py input.txt 100`.

The goal is to select a subset of the items to maximize the payoff such that the cost is below some
threshold. That is, the output should be a set of items (identified by number) that solves the
Knapsack problem. It's also worth outputting the total cost and value of these items. This can all
just be printed and may look something like below.
'''
### needs to be finished ###
import timing
import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(item, capacity):
    # Your code here

    pass

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))

    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')


### Class Notes ####

### Niave approach, simplest ###
def naive_knapsack(weight_limit, items):
    items.sort(key=lambda x: x.value, reverse=True)
    # could be better if we sorted by value/weight ratio...
    sack = [] # create an empty list for sack
    cur_weight = 0
    for i in range(len(items)):
        # put the nxt most valuable item in it If there is room
        if cur_weight + items[i.weight <= weight_limit]:
            sack.append(items[i])

    return sack
    # log(n)

### Brute force approach,  check everything ###

#Brute Force Algorithms are exactly what they sound like – straightforward methods of solving
#a problem that rely on sheer computing power and trying every possibility rather than advanced
#techniques to improve efficiency.
# pros - it will find the best solution
# cons - it will take a REALLY long time

import itertools
def knapsack_brute_force(weight_limit, items):
    max_value = -1
    best_combo = None
    for i in range(1, len(items)+1):
        list_of_combos = list(combinations(items, i)) # create a list of combos use the combinations function on our items

        for item in combo:
            value = 0 # of the entire combo
            weight = 0 # of the entire combo
            for item in combo:
                value += item.vaue
                weight + item.weight
            if weight <= weight_limit: # could fit in knapsack
                if value > max_value:
                    max_value = value
                    best_combo = combo

    return best_combo

### Greedy approach,  check everything ###
# pros - much faster than Brute Force, much smarter than Niave
# cons - may not get optimal result
'''
Greedy is an algorithmic paradigm that builds up a solution piece by piece, always choosing
the next piece that offers the most obvious and immediate benefit. So the problems where
choosing locally optimal also leads to global solution are best fit for Greedy.

For example consider the Fractional Knapsack Problem. The local optimal strategy is to choose
the item that has maximum value vs weight ratio. This strategy also leads to global optimal solution
because we allowed to take fractions of an item.
'''
def knapsack_greedy(weight_limit, items):
    for i in items: # for an item in items
        i.efficiency = i.value / i.weight_limit

    items.sort(keys=lambda x: x.efficiency, reverse=True)

    sack = [] # create an empty list for the sack
    weight = 0 # set the weight to 0
    for i in items: # for an item in items
        weight += i.weight
        if weight > weight_limit:
            return sack
        else:
            sack.append(i)

    return sack

# Fibinacci sequence
def fib(n):

#Fibonacci Sequence:
#The Fibonacci numbers are the numbers in the following integer sequence.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation.
    # base case
    if n == 1 or n == 0:
        return 1
    # recursive case
    else:
     return fib(n-1) + fib(n-2)

print('-----Fibinacci Base------')
print(fib(5))
print(fib(15))
print(fib(30))
print(fib(35))

# Recursive Fibonacci - with Memoization
'''
Memoization:
memoization or memoisation is an optimization technique used primarily to speed up computer
programs by storing the results of expensive function calls and returning the cached result
when the same inputs occur again.
'''
def fib_mem(n, cache = {}):
    # base case
    if n == 1 or n == 0:
        return 1
    # recursive case
    elif n in cache.keys():
        return cache[n]
    else:
        value = fib_mem(n-1) + fib_mem(n-2)
        cache[n] = value
        return value

print('-----Memoization------')
print(fib_mem(5))
print(fib_mem(15))
print(fib_mem(30))
print(fib_mem(35))
# Recursive Fibonacci - with Memoization

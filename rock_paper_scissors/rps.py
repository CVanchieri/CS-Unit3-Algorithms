
'''
Rock Paper Scissors:

Write a function `rock_paper_scissors` to generate all of the possible plays that can be made
in a game of "Rock Paper Scissors", given some input `n`, which represents the number of plays per round.

For example, given n = 2, your function should output the following:
python
[['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

Your output should be a list of lists containing strings. Each inner list should have length equal to the input n.
'''
### complete ###
import timing
import sys
def rock_paper_scissors(n): # Elapsed time: 0:00:00.002649
  # Your code here
  options = [['rock'], ['paper'], ['scissors']]
  if n == 0: # if the n value is equal to 0
    return [[]] # return an empty list

  if n == 1: # if the n value is equal to 1
    return options # return the original options list

  output = [] # create an output list
  for result in rock_paper_scissors(n-1):
    for option in options: # for an option in options
      output.append(result + option) # append the result and option value to the output list

  return output # return the output list

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

'''
### 2nd option ###

'''

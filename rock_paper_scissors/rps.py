
#!/usr/bin/python
### complete ###
import sys
def rock_paper_scissors(n):
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

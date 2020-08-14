
'''
Single Number:
Given a non-empty array of integers where every element appears twice except for one.
Find that single number. You may assume that there will _always_ be _one_ odd-number-out
and every other number in the input shows up exactly twice.

Examples
Sample input: [2, 2, 1]
Expected output: 1

Sample iput: [4, 1, 2, 1, 2]
Expected output: 4
'''
'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
import timing
### complete ###
def single_number(arr): # Elapsed time: 0:00:00.029485
    # Your code here
    for i in arr: # for value in arr
        dupe = 0 # set dupe to 0
        for v in arr: # for value in arr
            if i == v: # if i value is equal to v value
                dupe += 1 # add 1 to the dupe
                if dupe > 1: # if dupe is greater than 1 stop
                    break
        if dupe == 1: # if dupe is equal to 1
            return i # return the value

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

'''
### 2nd option ###
def single_number(arr): # Elapsed time: 0:00:00.048531
    # Your code here
    single = [] # create a single list

    for x in arr: # for the value in arr
        single_index = None # single_index set to None
        for i in range(len(single)): # for value in the rangle of the length of the single list
            if single[i] == x: # if the single value is equal to x value
                single_index = i # set single_index to the i value
                next
        if single_index == None: # if the single_index is equal to None
            single.append(x) # append the x valie to the single list
        else: # else
            single.pop(single_index) # pop off the single_index from the single list

    return single[0] # return the intial value of the single list

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
'''

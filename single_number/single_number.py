'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
### complete ###
def single_number(arr):
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

'''
Input: a List of integers
Returns: a List of integers
'''
### complete ###
def moving_zeroes(arr):
    # Your code here
    low = [] # create a list for negative numbers
    high = [] # create a list for positive numbers

    for i in arr: # iterate through the arr list
        if i <= 0: # if value is  less than or equal to 0
            low.append(i) # append the value to the low list
            low.sort() # sort the low list

        elif i > 0: # else if value is greater than 0
            high.append(i) # append the value to the high list

        elif len(low) and len(high) == 0: # else if the length of low and the length of high are equal to 0
            return arr # return original list

    return high + low # return high and low list

if __name__ == '__main__':
    # use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

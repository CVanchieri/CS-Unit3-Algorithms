'''
Moving Zeroes:
Write a function that takes an array of integers and moves each non-zero integer to
the left side of the array, then returns the altered array. The order of the non-zero
integers does not matter in the mutated array.

## Examples
Sample input: [0, 3, 1, 0, -2]
Expected output: 3
Expected output array state: [3, 1, -2, 0, 0]
'''
'''
Input: a List of integers
Returns: a List of integers
'''
import timing
### complete ###
def moving_zeroes(arr): # Elapsed time: 0:00:00.002907
    # Your code here
    run = True # set run to True
    count_zero = 0 # set count_zero to 0
    while run: # while run 'True'
        for i, v in enumerate(arr): # for the value and index of value in the array
            if v == 0: # of value is equal to 0
                arr.insert(len(arr), v) # insert the value into the arr with the length of the arr
                arr.pop(i) # pop off the index on the array
                count_zero += 1 # add 1 to the count_zero

        if count_zero == len(arr): # if count_zero is equal to the length of the array
            return arr # return the array

        if arr[0] == 0: # if the intial array value is equal to 0
            run = True # set run to True

        else: # else
            run = False # set run to False

    return arr # return the arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    #arr = [0, 0, 0, 0, 0]
    arr = [0, 3, 1, 0, -2]
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")

'''
### 2nd option ###
def moving_zeroes(arr): # Elapsed time: 0:00:00.003659
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
'''

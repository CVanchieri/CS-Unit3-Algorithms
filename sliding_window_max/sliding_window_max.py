'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
### need to finish the 'large input test' ###
def sliding_window_max(nums, k):
    # Your code here
    storage = [] # create a storage list
    for i in range(len(nums) - (k-1)): # fir value in the range from the (length of nums) minus (k value -1)
        max = max(nums[i:i+k]) # set max equal to the i value + k value
        storage.append(max) # append the max value to the storage list

    return storage # return the storage list

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")

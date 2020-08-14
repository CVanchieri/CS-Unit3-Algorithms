
'''
Sliding Window Max:
Given an array of integers, there is a sliding window of size `k` which is moving from the left side of the array to the right, one element at a time. You can only interact with the `k` numbers in the window. Return an array consisting of the maximum value of each window of elements.

Example
Sample Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Expected Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 Can you implement a solution that calculates all of the maximum sliding window values in O(n) time?
'''
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
### Complete, runs test max file but fails for time on test max large input ###
import timing
def sliding_window_max(nums, k): # Elapsed time: 0:00:00.003095
    # Your code here
    slide = [] # create a slide list
    max_slide = [] # create a max slide list
    for i in range(k): # for value in range of k value
        slide.append(nums[i]) # append nums value to the slide list

    for i in nums[k:]: # for value in nums
        max_slide.append(max(slide)) # append max slide value to the max_slide list
        slide.pop(0) # pop off initial value of slide list
        slide.append(i) # append i value to the slide list

    max_slide.append(max(slide)) # append the max slide value to the max_slide list

    return max_slide # return the max_slide list

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
'''
### Option 2 ###
# only works with -k small
def sliding_window_max(nums, k): # Elapsed time: 0:00:00.002455
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
'''

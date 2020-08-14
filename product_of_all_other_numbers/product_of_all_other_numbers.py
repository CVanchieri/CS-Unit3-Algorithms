
'''
Product of All Other Numbers:
Write a function that receives an array of integers and returns an array consisting
of the product of all numbers in the array _except_ the number at that index.

For example, given
[1, 7, 3, 4]
your function should return
[84, 12, 28, 21]
by calculating
[7*3*4, 1*3*4, 1*7*4, 1*7*3]

In the above example, the final value at index 0 is the product of every number in the input array _except_ the number at index 0.
Can you do this in `O(n)` time with `O(n)` space _without_ using division?
'''
'''
Input: a List of integers
Returns: a List of integers
'''
import timing
### complete ###
def product_of_all_other_numbers(arr): # Elapsed time: 0:00:00.002717
    # Your code here
    products = [] # create a products list
    for i in range(len(arr)): # for the value in the range of the length of the arr
        product = 1 # set the product equal to 1

        for j in range(len(arr)): # for value in the rangle of the length of the arr
            if j != i: # if the j value is not equal to i value
                product *= arr[j] # multiple product by the j value in arr
        products.append(product) # append the product value to the products list

    return products # return the products list

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

'''
### 2nd option ###
import numpy
def product_of_all_other_numbers(arr): # Elapsed time: 0:00:03.680691
    # Your code here
    new_arr = []
    for i, _ in enumerate(arr):
        if i == 0:
            lst2 = arr[i+1:]
            new_arr.append(numpy.prod(lst2))
        else:
            lst1 = arr[:i]
            lst2 = arr[i+1:]
            lst3 = lst1 + lst2
            new_arr.append(numpy.prod(lst3))

    return new_arr

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 2, 3, 4, 5]
    # arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
'''

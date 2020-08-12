
'''
Input: a List of integers
Returns: a List of integers
'''
### complete ### 
def product_of_all_other_numbers(arr):
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

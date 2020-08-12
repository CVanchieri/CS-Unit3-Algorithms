
"""
Input: an integer
Returns: an integer
"""
### complete ###
def eating_cookies(n, p=[]):
    if n <= 1: # if the n value is less than 1
        return 1 # return 1
    else: # else
        num_ways = [0] * (n + 1) # set num_ways to 0 multiplied by (n value and 1)
        num_ways[0] = 1 # set num_ways initial value to 1
        num_ways[1] = 1 # set num_ways 2nd value to 1
        num_ways[2] = 2 # set num_ways 3r value to 2

        for i in range(3, n + 1): # for the value in range from 3 through (n value + 1)
            num_ways[i] = num_ways[i - 1] + num_ways[i - 2] + num_ways[i - 3] # set num_ways value index to num_ways value index minus 1 and
                                                                              # num_ways value index minus 2 and num_ways value index minus 3
        return num_ways[n] # return the num_ways index n value

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies"
    )

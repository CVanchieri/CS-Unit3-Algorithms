
'''
Eating Cookies:
Cookie Monster can eat either 1, 2, or 3 cookies at a time. If he were given a jar of
cookies with `n` cookies inside of it, how many ways could he eat all `n` cookies in
the cookie jar? Implement a function `eating_cookies` that counts the number of possible
ways Cookie Monster can eat all of the cookies in the jar.

For example, for a jar of cookies with `n = 3` (the jar has 3 cookies inside it), there
are 4 possible ways for Cookie Monster to eat all the cookies inside it:

 1. He can eat 1 cookie at a time 3 times
 2. He can eat 1 cookie, then 2 cookies
 3. He can eat 2 cookies, then 1 cookie
 4. He can eat 3 cookies all at once.

Thus, `eating_cookies(3)` should return an answer of 4.

Can you implement a solution that runs fast enough to pass the large input test?
'''
"""
Input: an integer
Returns: an integer
"""
import timing # calculates runtime
### complete ###
def eating_cookies(n, p=[]): # Elapsed time: 0:00:00.003633
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

'''
### 2nd option ###
def eating_cookies(n): # Elapsed time: 0:00:00.003702
    if n == 0:
        return 1
    elif n == -1:
        return 0
    elif n == -2:
        return 0
    eat1 = eating_cookies(n-1)
    eat2 = eating_cookies(n-2)
    eat3 = eating_cookies(n-3)

    return eat1 + eat2 + eat3

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 3

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
'''

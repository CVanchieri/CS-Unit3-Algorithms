# Ex. 1
# Given the radius of a circle, calculate it's area and format
# the result to three decimal places

### what questions are there? ###

# what is the output wanted?
# what is the formula for area


# A = PI * r^2
# use exact value of PI - math.pi
# format output as a string
import math

def area_circle(radius):
    # do math to calc area
    area = math.pi * radius * radius
    # format the result
    result = f'{area:.3f}'

    return result

print(area_circle(3))   # 28.274
# Ex. 2
# We'll say that a positive int divides itself if every digit in the
# number divides into the number evenly. So for example 128 divides
# itself since 1, 2, and 8 all divide into 128 evenly.
# And we'll say that 0 does not divide into anything evenly, so no
# number with a 0 digit divides itself.
# Write a function to determine if a number divides itself.
# [source - https://codingbat.com/prob/p165941]

### Questions ###

# check in value contains a 0
# store value in seperate variable
#
# boolean variable that results to true
# list cpmprehensions

# turn value into list, num

# iterate



def divides_self(num):
    # copy num
    digits_left = num
    # loop through all digits in num
    while digits_left > 0:
        # num % 10 to GET the dight on the RHS
        digit = digits_left % 10
        # if that result is 0, return false
        # if num % result is NOT 0, return false
        if digit == 0 or num % digit != 0:
            return False
        # // 10 to chop off the digit on the RHS
        digits_left //= 10 # digits_left // 10

    # if all digits divide num evenly, return true
    return True

    pass
print(divides_self(128)) # → True
print(divides_self(12)) # → True
print(divides_self(571)) # → False
print(divides_self(120)) # → False

# Ex. 3
# The Knapsack Problem
# https://en.wikipedia.org/wiki/Knapsack_problem


# we want to maximize $$ value while staying at or under the weight (kg) limit
# no volume constraint
# each item only exists once (no duplicates)


# limit = 15kg

### Naive solution ### easiest, not the best typically

def naive_knapsack(weight_limit, items):
    items.sort(key=lambda x: x.value, reverse=True)
    # could be better if we sorted by value/weight ratio...
    sack = []
    cur_weight = 0
    for i in range(len(items)):
    # put the next valuable item in it IF there is room
        if cur_weight + items[i].weight <= weight_limit:
            sack.append(items[i])

    return sack

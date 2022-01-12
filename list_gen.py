#MAIN SOLUTION:

import math

"""
Converts Decimal to Binary. 
"""


def decimalToBinary(n, places):
    return bin(n)[2:].zfill(places)


"""
Generator function that yields subset of the set of integers between 0 and n-1.
Input: size of the set we compute the subset of.
Output: Iterator of the subset. Returns list of values belonging to subset.
"""


def generate_sub_set(set_size):
    subset = []
    for x in range(0, size):
        subset.append(x)
    print('Subsets for {0} are'.format(subset))
    yield []
    pow_set_size = int(math.pow(2, set_size))
    for counter in range(1, pow_set_size):
        value = decimalToBinary(counter, set_size)
        a = []
        for index, char in enumerate(value):
            if char == '1':
                a.append(subset[index])
        yield a


print('Please enter the set size')
# Input
size = int(input())

for cur_list in generate_sub_set(size):
    print(cur_list)


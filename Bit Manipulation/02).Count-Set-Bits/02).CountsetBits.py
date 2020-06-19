"""
Write A program to count number of 1's in a binary representation of an integer.
"""

def count_bits(n):

    count = 0
    while(n) :
        count += n & 1
        n >>= 1

    return count


ans = count_bits(3)
print("The number of set bits in 3 is {}".format(ans))

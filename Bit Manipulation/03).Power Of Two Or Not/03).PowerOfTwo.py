"""
iven a positive integer, write a function to find if it is a power of two or not.

Note:-
A number which is a power of two will always have one as set bit.
"""

#Function to count the number of set bits of an integer in binary form.
def count_bits(n):
    count = 0
    while(n):

        count += n & 1
        n >>= 1

    return count


def check(n):

    ans =count_bits(n)

    if ans == 1:
        return True

    else:
        return False


if(check(13)):
    print("13 is  a power of two\n")

else:
    print("13 is not a power of two\n")


if(check(16)):
    print("16 is  a power of two\n")

else:
    print("16 is not a power of two\n")

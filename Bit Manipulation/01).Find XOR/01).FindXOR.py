"""
Given a number n, the task is to find the XOR.
"""
def findxor(n) :

    if  n% 4 == 0:
        return n

    elif n % 4 == 1:
        return 1

    elif n % 4 == 2:
        return n + 1

    else:

        return 0


ans  = findxor(4)
print("the XOR of {} is {}".format(4,ans))

ans = findxor(9)
print("the XOR of {} is {}".format(9,ans))

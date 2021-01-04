"""
Given digit = 7,bits = 3
output = 111
Given digit = 7,bits = 4
output = 0111
Given digit = 7,bits = 2
ouput = error
"""

digit = int(input("Enter the digit"))
bits = int(input("Enter the number of bits"))

#bin is an inbuilt function to convert decimal to binary
#binaryForm=bin(digit)[2:]

#Function to generate binary number 
def generate_binary( digit ):
    if digit == 0:
        return 0
    else:
        return (digit % 2 + 10 *
                generate_binary(int(digit // 2)))


binaryForm = str(find(digit))

if bits< len(binaryForm):
    print("Invalid number of bits to print {} in binary".format(digit))

else:
    print("0"*(bits-len(binaryForm))+binaryForm)

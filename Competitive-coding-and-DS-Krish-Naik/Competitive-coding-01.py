"""
Generate All Binary Strings
if n=2 ['00', '01', '10', '11']
if n=3 ['000', '001', '010', '011', '100', '101', '110', '111']
if n=4 ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
"""

n = int(input("Enter the number whose binary "))

def append_element(x,l):
    return [x + element for element in l]

def generate_bits(n):
    if n == 0:
        return []
    elif n == 1:
        return ["0","1"]

    else:
        return (append_element("0",generate_bits(n-1))+
        append_element("1",generate_bits(n-1)))


print(generate_bits(n))

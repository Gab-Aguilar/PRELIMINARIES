""""GLLAguilar
    DATALOG Lab06
    MAR. 4, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
print("MUST BE A POSITIVE INTEGER.") #prints the sentence.
m = int(input("1st Value: ")) #inputs the firts value.
n = int(input("2nd Value: ")) #inputs the second value.

def multiply(m, n): #defines the number to be multiplied
    if m < n: #if the value of m is less than the value of n.
        return multiply(n, m) #the value will multiply.
    elif n != 0: #if the number n is not equal to zero.
        return (m + multiply(m, n - 1)) #the value will go through the equation and multiply.
    else:
        return 0

print('ANSWER: ',multiply(m, n)) #prints the answer.
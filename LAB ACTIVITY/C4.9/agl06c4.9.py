""""GLLAguilar
    DATALOG Lab06
    MAR. 4, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
B = [1, 2, 3, 4, 5, 9, 10] #the given value/set.
def mins(B, z): #defines the minimum value of the set.
    if z == 1: #has been traversed
        return B[0]
    return min(B[z - 1], mins(B, z - 1)) #equation to get the minimum value inside the set

def maxs(B, z): #defines the maximum value of the set
    if z == 1: #has been traversed
        return B[0]
    return max(B[z - 1], maxs(B, z - 1)) #equation to get the maximum value inside the set.

if __name__ == '__main__': #driver code.
    z = len(B) #counts the value.
    print('Minimum: ',mins(B, z)) #prints the minimum number.
    z = len(B) #counts the value
    print('Maximum: ',maxs(B, z)) #prints the maximum number.

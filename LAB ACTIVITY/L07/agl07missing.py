""""GLLAguilar
    DATALOG Lab07
    MAR. 18, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
def missing(array, first, last): #defines the array, first and the last group of the array.
    if (first > last):
        return last + 1

    if (first != array[first]): #denotes if the first is group is not equal to the first array
        return first;

    mid = int((first + last) / 2) # divies the first and the second half into 2 groups.

    if (example[mid] == mid):  # defines value from 0 to mid since Left half has all elements
        return missing(array, mid + 1, last)

    return missing(array, first, mid)

example = [0, 1, 5, 7, 5, 5, 8, 7, 11] # to test above the function.
n = len(example) # to test above the function.
print("Smallest missing value", missing(example, 0, n - 1)) # to test above thefunction and prints the smallest value missing in the array.
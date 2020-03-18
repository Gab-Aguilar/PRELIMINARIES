""""GLLAguilar
    DATALOG Lab06
    MAR. 4, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
str = 'ojweotjvwpev' #given value

def vowel(ts): #defines the vowel
    return ts.upper() in ['A', 'E', 'I', 'O', 'U'] #returns the vowels

def consonant(ts): #defines consonants
    ts = ts.upper()
    return not ts == 'A' or ts == 'E' or ts == 'I' or ts == 'O' or ts == 'U' and ord (ts) >= 65 and ord(ts) <= 90 #defines the consonants

def countv(str): #defines the number of vowels
    count = 0
    for i in range(len(str)):
        if vowel(str[i]):
            count += 1
    return count
print('NUMBER OF VOWELS: ',countv(str)) #prints the number of vowels.

def number_of_consonants(str):
    count = 0

    for i in range(len(str)):
        if (consonant(str[i])):
            count += 1
    return count

print('NUMBER OF CONSONANTS: ',number_of_consonants(str)) #prints the number

def str(str):
    if countv(str) > number_of_consonants(str):
        print("There are more Vowels than Consonants.")
    else:
        print('There are more Consonants than Vowels')
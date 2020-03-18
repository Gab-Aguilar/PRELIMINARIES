""""GLLAguilar
    DATALOG Lab02
    FEB. 5, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
print("'+' ADDITION")
print("'-' SUBTRACTION")
print("'/' = DIVISION")
print("'*' MULTIPLICATION")

a = float(input()) #to input the firt number.
b = input() #to input the operator.
c = float(input()) #to input the second number.

if b == '+': #It indicates the operator to be used.
   n = a + c #it indicates the equation.
   print(int(n)) #it prints the answer to the equation
elif b == '-': #It indicates the operator to be used.
   m = a - c #it indicates the equation.
   print (int(m))#it prints the answer to the equation
elif b == '/': #It indicates the operator to be used.
   x = a // c #it indicates the equation.
   print(int(x)) #it prints the answer to the equation
elif b == '*': #It indicates the operator to be used.
   r = a * c #it indicates the equation.
   print(int(r)) #it prints the answer to the equation


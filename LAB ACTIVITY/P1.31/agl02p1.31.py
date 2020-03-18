""""GLLAguilar
    DATALOG Lab02
    FEB. 5, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""

charge = float(input("AMOUNT CHARGED: ")) #to be able to input whole number with decimals.
amount = float(input('AMOUNT PAID: ')) #to be able to input whole number with decimals.

c = amount - charge #equation
print("-----------------------------------")
print("WITH A TOTAL AMOUNT OF:",c) #to be able to print the answer of the equation.
print("-----------------------------------")

div1 = c//1000 #to divide the value of the variable 'c'.
c = c % 1000 #to get the remainder so that the other existing value will be the one to divide it and it will count on the amount where the remainder will reach 0.
div2 = c//500
c = c%500
div3 = c//200
c = c%200
div4 = c//100
c = c%100
div5 = c//50
c = c%50
div6 = c//20
c = c%20
div7 = c//10
c = c%10
div8 = c//5
c = c%5
div9 = c//1
c = c%1
div10 = c//.25
c = c%.25
div11 = c//.10
c = c%.10
div12 = c//.05
c = c%.05

print ("Number of Php 1000.00 bill/s: ",int(div1)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 500.00 bill/s: ",int(div2)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 200.00 bill/s: ",int(div3)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 100.00 bill/s: ",int(div4)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 50.00 bill/s: ",int(div5)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 20.00 bill/s: ",int(div6)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 10.00 bill/s: ",int(div7)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 5.00 bill/s: ",int(div8)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 1.00 bill/s: ",int(div9)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 0.25 bill/s: ",int(div10)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 0.10 bill/s: ",int(div11)) #to be able to print the number of bill/s in each valiue.
print ("Number of Php 0.05 bill/s: ",int(div12)) #to be able to print the number of bill/s in each valiue.



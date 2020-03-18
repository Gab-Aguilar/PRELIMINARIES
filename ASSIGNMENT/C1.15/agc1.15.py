def diff(list): #def function that defines the given set.
  b = set() #initializes an empty set.
  for g in list: #function that determines the set whether they are distinct or not.
    if g in b: #if statement, if there are same elements in the list.
      return False #prints false.
    b.add(g) #it adds a given element which is not in the list.
  return True #prints True.

print("---------------------------------------------------")
print("DETERMINES WHETHER THE GIVEN SET IS DISTINCT OR NOT")
thelist_1 = [1,2,3,4] #sample list
print(thelist_1) #prints 'thelist'.
print(diff(thelist_1)) #prints whether the set is distinct/TRUE or not distinct?FALSE
print("---------------------------------------------------")


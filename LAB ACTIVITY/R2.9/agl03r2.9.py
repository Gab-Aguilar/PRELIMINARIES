""""GLLAguilar
    DATALOG Lab03
    FEB. 12, 2020
    I have neither received nor provided any help
    on this (lab) activity, nor have I concealed
    any violation of the Honor Code.
"""
class Vector:

    def __init__(self,d): #constructor method
        self.coords = [0] * d

    def __len__(self):
        return len(self.coords)#constructor method

    def __getitem__(self,j):#constructor method
        return self.coords[j]

    def __setitem__ (self,j,val):#constructor method
        self.coords[j] = val

    def __add__ (self,other):#constructor method
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] + other[j]
        return result

    def __sub__(self, other):#constructor method
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    def __eq__ (self,other):#constructor method
        return self.coords == other._coords

    def __ne__(self,other):#constructor method
        return not self == other

    def __str__(self):#constructor method
        return '<' + str(self.coords)[1:-1] + '>'

    def __neg__(self):#constructor method
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __lt__(self, other): #constructor method
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self.coords < other.coords

    def __le__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self.coords <= other.coords



if __name__ == "__main__":

    v = Vector(5)  #it creates a "0, 0, 0, 0, 0"
    v[1] = 23  #'23' adds up to the set '0,0,0,0,0.
    v[-1] = 45  #'45' adds up to the set of '0,23,0,0,0.
    print(v[4])
    u = v + v #it initializes equation
    print(u)
    w = v - u #it initializes equation
    print(w)
    total = 0
    for entry in v: 
        total += entry
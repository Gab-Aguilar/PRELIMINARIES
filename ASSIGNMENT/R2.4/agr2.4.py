class Flower:
    def __init__(item, name, petals, price):  #constructor method
        item.name = name
        item.petals = petals
        item.price = price

    def set_value(item, newname, newpetals, newprice): #constructor method
        item.name = str(newname)
        item.petals = int(newpetals)
        item.price = float(newprice)

    def get_value(item):
        print (item.name, item.petals, item.price)

f1 = Flower ('Sampaguita', 12,10.00) # initialize values
f1.get_value()#get initialized values

f1.set_value('Sunflower',10,250.25) #change values 1
f1.get_value()#get new values 1

f1.set_value('Tulip',9,300.45) #change values 2
f1.get_value() #get new values 2


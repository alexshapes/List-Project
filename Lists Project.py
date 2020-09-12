
coffee_order = [
    "Dana - Flat White",
    "Mitzi - Hot Chocolate",
    "Alex - Tall Late",
    "Dana1 - Flat White",
    "Mitzi1 - Hot Chocolate",
    "Alex1 - Tall Late",
]
print(coffee_order)

additional_stuff = ["Whisky", "Beer", "Juice"]

shutdown = False
while (shutdown == False):

    print ("Menu. Please select from the following 5 options")
    print ("1 = Remove")
    print ("2 = Reverse")
    print ("3 = Sort")
    print ("4 = Count")
    print ("5 = Extend")
    userchoice = int(input ("What would you like to do?: "))

    if (userchoice == 1):
        print(coffee_order.remove("Alex1 - Tall Late"))
        print (coffee_order)
    elif (userchoice ==2):
        print(coffee_order.reverse())
        print("Reversed List : ",coffee_order)
    elif (userchoice ==3):
        print (coffee_order.sort())
        print ("Sorted List : ", coffee_order)
    elif (userchoice ==4):
         x = len(coffee_order)
         print ("coffees in total : ",x)
    elif (userchoice ==5):
        print (coffee_order.extend(additional_stuff))
        print(coffee_order)


    shutdown = False

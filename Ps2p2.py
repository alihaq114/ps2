print("Which Item did you buy Item A or B? ")
item = input()
print("Enter Quantity")
qty = float(input())
if item == "A":
    up = 10.0
else:
    up = 20.0
exp = qty * up
print("You bought " + item + " Unit Price = " + str(up) + "and total cost = " + str(exp))

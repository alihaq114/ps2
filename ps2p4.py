print("Enter name")
name = input()
print("enter cost")
cost = int(input())
if cost <= 1000:
    war = 0.005
else:
    war = 0.01
total = cost * war
print("your name is" + name)
print("The cost of warantee is " + str(war))
print("total cost is " + str(total))

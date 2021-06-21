print("enter user last name")
lastName = input()
print("enter number of dependents")
nod = float(input())
print("enter gross income")
gi = float(input())
ngi = gi - nod * 12000
if ngi >= 50000:
    tax = 0.01
else:
    tax = 0.02
it = ngi * tax
print("Your last name is: " + lastName)
print("Your gross income: " + str(gi))
print("Your Number of dependents: " + str(nod))
print("your adjusted gross income: " + str(ngi))
print("your income tax: " + str(it))

print("enter the quantity")
qty = float(input())
if qty >= 1000:
    up = 3.0
else:
    up = 5.0
extprice = qty * up
tax = extprice * 0.007
total = extprice + tax
print(" Quantity ordered " + str(qty))
print("unit price " + str(up))
print("Entended Price " + str(extprice))
print("Tax " + str(tax))
print("total order " + str(total))

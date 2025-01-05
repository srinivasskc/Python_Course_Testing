
total_cost = float(input("Enter the total cost of items shopped: "))

print("Cost of all items: ",total_cost)

if total_cost > 99.99:
    if total_cost >= 100 and total_cost <= 199.99:
        discount = 5
    elif total_cost >= 200 and total_cost <= 299.99:
        discount = 10
    elif total_cost >= 300 and total_cost <= 399.99:
        discount = 15
    elif total_cost >= 400 and total_cost <= 499.99:
        discount = 20
    elif  500 <= total_cost  <= 599.99:
        discount = 25
    else:
        discount = 30
    print("Discount is: %.2f rs" % discount)
    total_amount = total_cost - discount
    print("Total amount to pay is: ", total_amount)
else:
    print("Your Total Amount is: ", total_cost ," ,You are not eligible for discount")

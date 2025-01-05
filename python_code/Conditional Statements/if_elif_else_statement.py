'''
Enter name of the customer:
Enter the total cost of items shopped:

If the total cost > 100 and cost <= 199:
    customer should get 5/- discount
If the total cost > 200 and cost <= 299:
    customer should get 10/- discount
If the total cost > 300 and cost <= 399:
    customer should get 15/- discount
If the total cost > 400 and cost <= 499:
    customer should get 20/- discount
If the total cost > 500 and cost <= 599:
    customer should get 25/- discount
'''

customer_name = input("Enter the name of customer: ")
total_cost = float(input("Enter the total cost of items shopped by " + customer_name + ": "))

print("Cost of all items: ",total_cost)


if total_cost > 100 and total_cost <= 199.99:
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

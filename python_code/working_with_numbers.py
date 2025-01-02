# Converting int to string
pizza_cost = 150
print("Cost of Pizza: " + str(pizza_cost))

# Convert string to float
burger_cost = input("What is the cost of Burger? ")
print(burger_cost)
print(float(burger_cost)+ 0.08)

# convert string to int
maid_amount = "4000"
print(maid_amount)
print(type(maid_amount))
print(int(maid_amount))  # Converted to int - only as output    
print(type(maid_amount)) # But does not totally change from string to int.

# Cannot convert floating point string to int
shoe_price = "999.99"
print(shoe_price)
print(type(shoe_price))
# print(int(shoe_price))  # Cannot Convert to int 


# convert float  to int
train_price = 555.56
print(train_price)
print(type(train_price))
print(int(train_price)) 



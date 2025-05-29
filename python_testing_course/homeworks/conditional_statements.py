"""
Movie Ticket Pricing System:

Rules: Child <=12 -> 50% discount, seniors >=60 -> 30% discount, others -> no discount
Day time shows before 5 PM -> 20% discount, after 5 PM -> no discount

Tasks:
a. Assign a hardcoded age of customer and a hardcoded show time (in 24-hour format).
b. Determine the base ticket price (e.g., $10).
c. Use conditional statements to apply discounts based on age and show time.
d. Print the final ticket price after applying all applicable discounts.
# Movie Ticket Pricing System
"""
# Hardcoded values for age and show time
CUSTOMER_AGE = 45  # Example age of the customer
TIME_OF_THE_DAY = 1600  # Example show time in 24-hour format (4 PM)
# Base ticket price
BASE_TICKET_PRICE = 12.0

if CUSTOMER_AGE <= 12:
    discount = 0.5  # 50% discount for children
elif CUSTOMER_AGE >= 60:
    discount = 0.3  # 30% discount for seniors
elif TIME_OF_THE_DAY < 1700:
    discount = 0.2
else:
    discount = 0.0

# Initialize final ticket price with base price
final_ticket_price = BASE_TICKET_PRICE * (1 - discount)
# 12.0 * (1 - 0.2) = 12.0 * 0.8 = 9.6
# Multiplying the base price by (1 - discount) → gives you the remaining price you actually pay

print(f'The final ticket price is: ${final_ticket_price}')  

print(f'The final ticket price is: ${final_ticket_price:.2f}')  # Format to 2 decimal places

# If Statement
age = 18
if age >= 18:
    print("You are an adult.")

# If-Else Statement
birth_age = 17
if birth_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# If-Elif-Else Statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print("------------------")

x = 10
y = 20
if x > 0 and y > 0:
    print("Both x and y are positive numbers.")

if x > 0 or y > 0:
    print("At least one of x or y is a positive number.")


if not x > y: # This checks if x is not greater than y
    print("x is not greater than y.")

print("------------------")
# Using pass statement
x = 5
if x > 10:
    pass
    # This is a placeholder for future code, but we do nothing here.
else:
    print("x is not greater than 10, so we do nothing here.")

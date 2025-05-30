print("Using continue in for loops - skips the rest of the loop for a specific condition")

for i in range(1,11):
    if i == 5:
        continue  # Skip the rest of the loop when i is 5
    print(i)  # This will print numbers from 1 to 10, skipping 5

print("-----")

print("Using break in for loops - exits the loop when a specific condition is met")

for i in range(1, 11):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)  # This will print numbers from 1 to 4, then exit the loop

print("-----")

print("Using continue and break in for loops")

for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the loop when i is 5
    if i == 8:
        break  # Exit the loop when i is 8
    print(i)  # This will print numbers from 1 to 4, then skip 5, and stop before printing 8

print("-----")

print("Check if a number is even or odd, and if it is greater than 15 and print it")
for i in range(1, 21):
    if i % 2 == 0:  # Check if the number is even
        continue  
    if i > 15: # Check if the number is greater than 15 
        break  
    print(i)  

print("-----")

for i in range(1, 7):
    if i % 7 == 0:
        print("Found a multiple of 7, breaking the loop")
        break  # Exit the loop if a multiple of 7 is found
else:
    print("No multiples of 7 found in the range 1 to 6")

print("-----")

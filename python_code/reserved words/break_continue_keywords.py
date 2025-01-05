
numbers = [1,2,3,4,5,6,7,8]

print("Start of the Loop with Continue")

for number in numbers:
    if number == 5:
        continue
    print(number)

print("End of the Loop \n")

print("Start of the Loop with Break")

for number in numbers:
    if number == 5:
        break
    print(number)

print("End of the Loop")

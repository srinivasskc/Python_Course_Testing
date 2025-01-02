'''
Augmented Assignment Operators:

+=  Addition Assignment
-=  Subtraction Assignment
*=  Multiplication Assignment
/=  Division Assignment
//=  Floor Division Assignment
**=  Exponential Assignment
%=  Modulus Assignment
'''

course ="Python Step by Step"
course +=" Tutorials"

print(course)


addition = 10 + 5
print(addition)

addition = addition + 5
print(addition)

addition += 5
print(addition)


# Operator Precedence.
results = 21 - 1 * (10 + 10)
print(results)


num1 = 5
num2 = 6

num2 += num1
# num2 = num2 + num1 => 11
print("addition of two numbers: " , num2)

num2 -= num1
# num2 = num2 - num1 => 11-5 = 6
print("subtraction of two numbers: " , num2)

num2 *= num1
# num2 = num2 * num1 => 6*5 = 30
print("Multiply of two numbers: " , num2)

num2 /= num1
# num2 = num2 / num1 => 30/5 = 6.0
print("Division of two numbers: " , num2)

num2 //= num1
# num2 = num2 / num1 => 6/5 = 1.0
print("Float Division of two numbers: " , num2)

num2 **= num1
# num2 = num2 ** num1 =>  1.0**5 = 1.0
print("Exponential of two numbers: " , num2)

num2 %= num1
# num2 = num2 % num1 =>  1.0%5 = 1.0
print("Modulus of two numbers: " , num2)

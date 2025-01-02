# Exponential - Right to Left

exp_res = 2 ** 3 ** 2
print(exp_res)
# Output - 512
# 3**2=9 then 2**9=512

# To get Left to Right, we use parenthesis.

exp_res1 = (2**3)**2
print(exp_res1)
# 2**3 = 8 Then 8**2=64
# Output: 64


# Arithmetic Operator Precedence
res2 = 4+6*3
print(res2)
# Output => 6*3=18, 18+4=22

res3 = (4+6)*3
print(res3)
# Output => 4+6=10, 10*3=30

# Check associativity when operator has same precedence.
# Left tO Right
res4 = 3*4/2*12
# Output => 12/2=6.0, 6.0*12=72
print(res4)

res5 = 3*4//2*12
print(res5)
# Output => 12//2=6, 6*12=72

# Check for Bitwise Operators Precedence.

res6 = 2 & 3 | 7 << 2
# First Left Shift, Right Shift and then Bitwise And.
print(res6)
# Output: 30  (Need to understand better, if required)

# Check for Bitwise and Logical Operators Precedence.
res7 = 2 & 3 and 2 | 4
# First 2&3 then 2|4 then (combine of and)
print(res7)
# Output: 6


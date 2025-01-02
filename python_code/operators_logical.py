print((100 > 25) and (100 > 50))
# Output: True

print((100 < 25) and (100 > 50))
# Output: False and True => False

print((100 < 25) or (100 > 50))
# Output: False or True => True

print(not(100 < 25) or not(100 > 50))
# Output: not(False) or not(True) => True or False => True

print(not(100 < 25) or not(100 > 50) and (100 > 75))
# Output: not(False) or not(True) and True => True or False and True => True and True => True



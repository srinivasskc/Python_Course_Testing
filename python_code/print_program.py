# print(*args, sep=' ', end='\n', file=None, flush=False)

print()

# This will print with space in between as default
print(1,2)

# This will print with Tab Space in between as default
print(1,2,sep='\t')

# This will print in new lines
print(3)
print(4)
print("Hi")

# This will print in same line with space in between. (5 & 6 and ends with no space)
print(5, end=' ')
print(6, end='')

# Print the information to File. "srinivas.txt"
# fp is file pointer

fp = open("srinivas.txt", 'w', encoding="locale")

print(1,2, file=fp)

# Flush
print("Hello - This is flush - false", flush=False)
print('Official repository of "SAMURAI: Adapting Segment Anything Model for Zero-Shot Visual Tracking with Motion-Aware Memory"',flush=False)


# Print the information to File. "srinivas.txt"
# fp is file pointer

# Specify the encoding parameter explicitly when using open().
fp = open("srinivas.txt", 'w', encoding="locale")

print(1,2, file=fp)

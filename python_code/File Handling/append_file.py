# Append only - (a)

# Open the file for writing
# File is created if it does not exist
# Cursor is placed at the end of the file


file = open('python_code\\File Handling\\srinivas.txt', 'a', encoding='utf-8')
# print(file)
file.write('\nThis is the fourth line\n')
file.write('This is the fifth line\n')

file = open('python_code\\File Handling\\srinivas.txt', 'r', encoding='utf-8')
print(file.read())
file.close()

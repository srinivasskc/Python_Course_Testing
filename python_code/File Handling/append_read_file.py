# Append and Read File - (a+)

# Open the file for reading and writing
# File is created if it does not exist
# Cursor is placed at the end of the file
# Data is added at the end of the file

file = open('python_code\\File Handling\\srinivas_a+.txt', 'a+', encoding='utf-8')
file.write('\nThis is the sixth line\n')
file.write('This is the seventh line\n')
file.write('This is the eighth line\n')

file = open('python_code\\File Handling\\srinivas_a+.txt', 'r', encoding='utf-8')
print(file.read())
file = open('python_code\\File Handling\\srinivas_a+.txt', 'a+', encoding='utf-8')
file.write('\nThis is the ninth line\n')

file = open('python_code\\File Handling\\srinivas_a+.txt', 'r', encoding='utf-8')
print(file.read())
file.close()

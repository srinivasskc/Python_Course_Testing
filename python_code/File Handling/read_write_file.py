# Read and Write - (r+)

# Open the file for reading and writing
# If the file does not exist, it will raise an I/O Error
# Cursor is placed at beginning of the file

# read() - reads entire file
# readlines() - read all lines and return them as as each line a string element in a list 
# readline(n) - read a line of the file. Does not read more than one line. Read atmost specified n bytes of data.

# Once file is read, we need to open the file again to read it.

file = open('python_code\\File Handling\\srinivas_rw_file.txt', 'r+', encoding='utf-8')
# read() - reads entire file
print(file.read())

# readlines() - read all lines and return them as as each line a string element in a list
file = open('python_code\\File Handling\\srinivas_rw_file.txt', 'r+', encoding='utf-8')
print(file.readlines())

# readline(n) - read a line of the file. Does not read more than one line. Read atmost specified n bytes of data.
file = open('python_code\\File Handling\\srinivas_rw_file.txt', 'r+', encoding='utf-8')
print(file.readline(10))

file.close()
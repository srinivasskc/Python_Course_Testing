# Write and Read - (w+)

# Open the file for reading and writing
# For Existing file, data is truncated and over-written
# Cursor is placed at beginning of the file

# Add some data to existing file.

file=open('python_code\\File Handling\\srinivas_wr_file.txt', 'w+', encoding='utf-8')
print(file.read())
file.write('This is the first line\n')
file.write('This is the second line\n')
file.write('This is the third line\n')

# Data is truncated and over-written

file=open('python_code\\File Handling\\srinivas_wr_file.txt', 'w+', encoding='utf-8')
print(file.read())

file.close()

"""
r+ = read and write: If file does not exists, will throw an error
r = read
w+ = write and read: If file does not exists, will create a new file

"""

file = open("./python_code/File Handling/srinivas_w+.txt", "w+", encoding="utf-8")

file = open("./python_code/File Handling/srinivas_w+.txt", "r+", encoding="utf-8")
file.write("This is the first line\n")
file.write("This is the second line\n")
file.write("This is the third line\n")

file = open("./python_code/File Handling/srinivas_w+.txt", "r+", encoding="utf-8")
print(file.read())
file.close()

file = open("./python_code/File Handling/srinivas_w+.txt", "r", encoding="utf-8")
print(file.readlines())
file.close()

print("====Using For Loop===")

file = open("./python_code/File Handling/srinivas_w+.txt", "r", encoding="utf-8")
for row in file:
    print(row)
file.close()

with open("./python_code/File Handling/srinivas_a+.txt", "a+", encoding="utf-8") as append_file, \
        open("./python_code/File Handling/srinivas_w+.txt", "w+", encoding="utf-8") as write_file:
    append_file.write("This is the fourth line\n")
    append_file.write("This is the fifth line\n")

    write_file.write("This is the first line\n")
    write_file.write("This is the second line\n")
    

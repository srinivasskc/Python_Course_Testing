# File Handling

# Opening a file

file = open('python_code\\File Handling\\srinivas.txt', 'w', encoding='utf-8')
# print(file)
name = input('Enter your name: ')
file.write('Welcome {} to srinivas.txt'.format(name))


file.writelines(['\nThis is the first line\n', 'This is the second line\n', 'This is the third line\n'])

file.close()

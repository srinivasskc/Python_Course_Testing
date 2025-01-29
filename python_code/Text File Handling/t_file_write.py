"""
w - write / w+ - write and read
a - append / a+ - append and read
"""

file = open('.//python_code//File Handling//srinitest.txt','w', encoding='utf-8')

file.write('Name \t  Age \t  Country \n')
file.write('----- \t ----- \t ----- \n')
file.write('Srinivas \t  35 \t  India \n')
file.write('Kadiyala \t  35 \t  USA \n')

file.close()

file = open('.//python_code//File Handling//srinitest.txt','w+', encoding='utf-8')

file.write('Name     \t  Age    \t  Country \n')
file.write('-----    \t -----   \t -----    \n')
file.write('Srinivas \t  35     \t  India   \n')
file.write('Kadiyala \t  35     \t  USA     \n')
file.write('skc      \t  25     \t  India   \n')

file.close()

print('\n')


file = open('.//python_code//File Handling//srinitest.txt','a', encoding='utf-8')

file.write('\nName     \t  Age    \t  Country \n')
file.write('-----    \t -----   \t -----    \n')
file.write('Teja     \t  36     \t  India   \n')
file.write('Suresh   \t  35     \t  USA     \n')
file.write('Surya    \t  37     \t  India   \n')

file.close()

with open('.//python_code//File Handling//srinitest.txt','a+', encoding='utf-8') as file:
    file.write('\nName     \t  Age    \t  Country \n')
    file.write('-----    \t -----   \t -----    \n')
    file.write('Ganesh   \t  30     \t  India   \n')
    file.write('Srujan   \t  35     \t  USA     \n')
    file.write('Surya    \t  37     \t  India   \n')
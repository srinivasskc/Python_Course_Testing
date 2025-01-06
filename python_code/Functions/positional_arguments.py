'''
In positional arguments, it is only check if the values are there in positions
and not about exact value and related key mappings.
No error will receive
'''

def greet_class_teacher(name,year):
    print(f"\t Hello {name} Teacher, Good Morning")
    print(f"\t Happy New Year {year}")


print("Start of the function")
greet_class_teacher(2025, 'srini')
print("End of the function")


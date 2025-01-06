'''
Parameters in your code:
In the function definition def greet_the_teacher(name, age):, name and age are parameters.
These parameters tell the function to expect two inputs when it is called.


Arguments in your code:
When you call the function with greet_the_teacher("Deepthi", "21"), "Deepthi" and "21" are arguments.
"Deepthi" gets assigned to the parameter name.
"21" gets assigned to the parameter age.
'''

def greet_the_teacher(name,age):
    print(f"\t Hello {name} Teacher, Good Morning")
    print(f"\t Happy {age} Birthday to you and")
    print("\t Happy New Year")


print("Start of the function")
greet_the_teacher("Deepthi","21")
print("End of the function")

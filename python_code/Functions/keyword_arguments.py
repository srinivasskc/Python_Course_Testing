# Here we can define as key value pair in arguments.

def greet_class_teacher(name,year):
    print(f"\t Hello {name} Teacher, Good Morning")
    print(f"\t Happy New Year {year}")


print("Start of the function")
greet_class_teacher(year=2025, name="Srinivas")
print("End of the function")

print("\n")


# Positional arguments cannot come after keyword arguments.
# Error is displayed

def greet_new_teacher(name,year):
    print(f"\t Hello {name} Teacher, Good Morning")
    print(f"\t Happy New Year {year}")


print("Start of the function")
#greet_new_teacher(year=2025, "Srinivas")
print("End of the function")


print("\n")

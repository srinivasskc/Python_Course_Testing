# Remove the value from argument and add as default value for "year"

def greet_the_teacher(name,year=2025):
    print(f"\t Hello {name} Teacher, Good Morning")
    print(f"\t Happy New Year {year}")


print("Start of the function")
greet_the_teacher("Deepthi")
print("End of the function")

print("\n")

# Remove the value from argument and add as default value for "name"
# Error is displayed for "Year" parameter. As first parameter is having default value
# So we need to give both default values
# But if we still pass arguments to the function, arguments will take prescedence.
def greet_new_teacher(name="Sridhar",year=2026):
    print(f"\t Hello {name} Teacher, Good Morning")
    print(f"\t Happy New Year {year}")


print("Start of the function")
greet_new_teacher("Deepthi",2025)
print("End of the function")


print("\n")

# Default Values to the function parameters
def greet_class_teacher(name="Vasudev",year=2025):
    print(f"\t Hello {name} Teacher, Good Morning")
    print(f"\t Happy New Year {year}")


print("Start of the function")
greet_class_teacher()
print("End of the function")

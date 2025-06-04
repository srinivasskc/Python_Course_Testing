def example_function_local():
    """
    This function demonstrates the scope of a local variable.
    """
    local_var = "I am a local variable"
    print(f"Inside the example function : {local_var}")
# This function demonstrates the scope of a local variable

example_function_local()
# print(f"Outside the example function: {local_var}")  # This will raise an error because local_var is not defined outside the function   

print("-----")

GLOBAL_VAR = "I am a global variable"

def example_function_global():
    """
    This function demonstrates the scope of a global variable.
    """
    print(f"Inside the example function global : {GLOBAL_VAR}")
# This function demonstrates the scope of a local variable

example_function_global()
print(f"Outside the example function global: {GLOBAL_VAR}")  
# This will not raise an error because global_var is defined outside the function


print("-----")
print("Example of modifying a global variable within a function")

global_variable = "I am a global variable"

def example_function_global_access():
    """
    The outer global is modified within the function., but outside the function it remains unchanged.
    """
    global_variable = "I am a modified global variable"
    # This line modifies the global variable within the function scope
    print(f"Inside the example function global access: {global_variable}")

example_function_global_access()
print(f"Outside the example function global access: {global_variable}")


print("-----")
print("Example of modifying a global variable within a function")

global_new_variable = "I am a global variable"

def example_function_global_modify():
    """
    The outer global is modified within the function., and outside the function value also calls the modified value.
    as global keyword is used.
    """
    global global_new_variable
    global_new_variable = "I am modified global variable"
    print(f"Inside the example function global modify: {global_new_variable}")

example_function_global_modify()
print(f"Outside the example function global modify: {global_new_variable}")
first_name="Srinivas"
last_name="Kadiyala"

# Formatting the Strings

# Way 1
name = f'{first_name} {last_name}'
print(name)
# Srinivas Kadiyala


# Way 2
greeting = '''Hello {}
How are you doing today?
I hope the weather is good ther.
Have a good day ahead!
'''

print(greeting.format(first_name))

# Way 3
greetings = f'''Hello {first_name}
How are you doing?
I hope you are doing good.
Have a good career!
'''

print(greetings)

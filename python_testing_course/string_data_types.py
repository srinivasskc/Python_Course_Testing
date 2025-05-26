str1 = "Hello,World!"
str2 = 'Python Testing Course'

# Print strings
print(str1, str2)

# Print String Characters based on Index Value.
print(str1[0])  
print(str1[1])  
print(str2[0])  
print(str2[2])  

# Length of the string
print(f"The length of str1 is {len(str1)} and length of str2 is {len(str2)}")

print(str1[11])
print(str2[20])

# Replace of String
new_str1 = str1.replace("World", "Python")
print(new_str1)

# Split
print(str1.split(",")) # Split by Comma
print(str2.split(" "))  # Split by space

# Combine
str3 = str1 + " " + str2
print(str3)

# Escape Characters
text = "Movie \"Home Alone\" is a great movie"
print(text)
text1 = "Movie 'Home Alone' is a great movie"
print(text1)

